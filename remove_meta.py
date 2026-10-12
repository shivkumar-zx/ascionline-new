import re

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div class="timeline-entry__meta"></div> globally
content = re.sub(r'<div class="timeline-entry__meta"></div>\s*', '', content)

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed all instances of timeline-entry__meta.")
