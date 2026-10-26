import bleach
import markdown


ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS).union(
    {"h2", "h3", "h4", "hr", "p", "pre"}
)
ALLOWED_ATTRIBUTES = {"a": ["href", "title"]}


def render_markdown(source):
    rendered = markdown.markdown(source, extensions=["fenced_code", "sane_lists"])
    return bleach.clean(
        rendered,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols={"http", "https", "mailto"},
        strip=True,
    )