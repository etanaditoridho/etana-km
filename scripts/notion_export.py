import os
import requests
import json
from datetime import datetime

NOTION_API_KEY = os.environ["NOTION_API_KEY"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_all_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    return response.json().get("results", [])

def get_page_content(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    response = requests.get(url, headers=headers)
    return response.json().get("results", [])

def block_to_markdown(block):
    t = block.get("type")
    if t == "paragraph":
        texts = block[t].get("rich_text", [])
        return " ".join([r.get("plain_text","") for r in texts])
    elif t == "heading_1":
        texts = block[t].get("rich_text", [])
        return "# " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "heading_2":
        texts = block[t].get("rich_text", [])
        return "## " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "heading_3":
        texts = block[t].get("rich_text", [])
        return "### " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "bulleted_list_item":
        texts = block[t].get("rich_text", [])
        return "- " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "numbered_list_item":
        texts = block[t].get("rich_text", [])
        return "1. " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "to_do":
        texts = block[t].get("rich_text", [])
        checked = block[t].get("checked", False)
        box = "[x]" if checked else "[ ]"
        return f"- {box} " + " ".join([r.get("plain_text","") for r in texts])
    elif t == "code":
        texts = block[t].get("rich_text", [])
        lang = block[t].get("language", "")
        code = " ".join([r.get("plain_text","") for r in texts])
        return f"```{lang}\n{code}\n```"
    elif t == "divider":
        return "---"
    return ""

def export_page(page):
    props = page.get("properties", {})
    name_prop = props.get("Name", {})
    rich = name_prop.get("title", [])
    title = " ".join([r.get("plain_text","") for r in rich]) if rich else "Untitled"

    status = ""
    if "Status" in props:
        sel = props["Status"].get("select")
        if sel:
            status = sel.get("name", "")

    category = ""
    if "Kategori" in props:
        sel = props["Kategori"].get("select")
        if sel:
            category = sel.get("name", "")

    page_id = page["id"]
    blocks = get_page_content(page_id)

    lines = [
        f"# {title}",
        f"",
        f"**Status:** {status}  ",
        f"**Kategori:** {category}  ",
        f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        "---",
        ""
    ]

    for block in blocks:
        md = block_to_markdown(block)
        if md:
            lines.append(md)

    return title, "\n".join(lines)

def write_log(exported):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/export_log.md"
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n## Backup {now}\n")
        for title in exported:
            f.write(f"- {title}\n")

def main():
    os.makedirs("wiki", exist_ok=True)
    pages = get_all_pages()
    exported = []

    for page in pages:
        title, content = export_page(page)
        safe_title = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)
        filepath = f"wiki/{safe_title}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        exported.append(title)
        print(f"Exported: {title}")

    write_log(exported)
    print(f"Done! {len(exported)} pages exported.")

if __name__ == "__main__":
    main()
