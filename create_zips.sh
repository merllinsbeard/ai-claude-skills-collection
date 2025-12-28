#!/bin/bash
cd /Users/merlin/Dev/ai-claude-skills-collection

for category in development scientific content business meta documents devops ai-ml automation; do
  echo "Processing $category..."
  if [ -d "$category" ]; then
    cd "$category"
    for skill_dir in */; do
      skill_name="${skill_dir%/}"
      if [ -d "$skill_name" ]; then
        echo "  Zipping: $skill_name"
        cd "$skill_name"
        zip -rq "$skill_name.zip" . -x "*.zip" -x ".DS_Store" -x "__pycache__/*" -x "*.pyc" -x "node_modules/*" -x "venv/*" -x ".venv/*" 2>/dev/null
        cd ..
      fi
    done
    cd ..
  fi
done

echo ""
echo "Done! Total zip files created:"
find . -name "*.zip" -type f | wc -l
