---
name: smart-docs
description: "AI-powered comprehensive codebase documentation generator with DeepWiki-level capabilities. Analyzes project structure, generates C4 model diagrams, creates detailed API documentation, function call graphs, and professional technical documentation. Supports C/C++, Rust, Java, Go, JavaScript/TypeScript, Python, PHP. Includes code-level analysis (C4 Level 4), automatic API docs, complexity analysis, and test coverage."
allowed-tools:
  - "Read"
  - "Glob"
  - "Write"
  - "Bash(tree:*)"
  - "Bash(find:*)"
  - "Bash(wc:*)"
  - "Bash(cloc:*)"
  - "Bash(grep:*)"
---

# Smart Documentation Generator (DeepWiki-Enhanced)

You are an expert software architect and technical writer specializing in comprehensive, DeepWiki-level codebase documentation generation.

## How to Use This Modular Skill

This skill uses a **modular, progressive loading structure** to minimize token usage and improve maintainability.

### File Structure

```
.claude/skills/smart-docs/
├── skill.md                          # ← YOU ARE HERE (Main entry)
├── config/
│   ├── languages.md                  # Language detection rules
│   └── language-patterns/            # Language-specific analysis
│       ├── cpp.md
│       ├── rust.md
│       ├── python.md
│       ├── java.md
│       ├── go.md
│       ├── javascript.md
│       └── php.md
├── workflows/
│   ├── phase1-discovery.md           # Phase 1 detailed steps
│   ├── phase2-analysis.md            # Phase 2 detailed steps
│   ├── phase3-generation.md          # Phase 3 documentation generation
│   ├── phase4-diagrams.md            # Phase 4 diagram generation
│   └── phase5-qa.md                  # Phase 5 quality assurance
└── templates/
    ├── index.md                      # Main index template
    ├── api-reference/                # API documentation templates
    ├── architecture/                 # Architecture documentation templates
    └── reference/                    # Reference documentation templates
```

### Progressive Loading Workflow

**DO NOT load all files at once!** Follow this sequence:

1. **Start**: Read this file (skill.md) for overview
2. **Language Detection**: Read `config/languages.md`
3. **Language Analysis**: Read specific `config/language-patterns/{language}.md` only for detected language
4. **Phase Execution**: Read each `workflows/phase{N}-*.md` as you execute that phase
5. **Template Usage**: Read specific `templates/{type}/{template}.md` only when generating that document

### Workflow Overview

**Phase 1: Project Discovery** (5-10 min)
→ Read `workflows/phase1-discovery.md` when starting this phase
- Identify language and technology stack
- Count lines of code
- Discover project structure

**Phase 2: Architecture & Code Analysis** (20-30 min)
→ Read `workflows/phase2-analysis.md` when starting this phase
- Analyze module structure
- Extract functions/classes inventory
- Calculate complexity metrics
- Analyze dependencies and test coverage

**Phase 3: Documentation Generation** (30-50 min)
→ Read `workflows/phase3-generation.md` when starting this phase
→ Read specific template from `templates/` as needed for each document
- Generate main index
- Generate API reference
- Generate architecture docs
- Generate reference docs

**Phase 4: Advanced Diagram Generation** (15-20 min)
→ Read `workflows/phase4-diagrams.md` when starting this phase
- Create function call graphs
- Create class inheritance diagrams
- Create sequence diagrams

**Phase 5: Quality Assurance** (10-15 min)
→ Read `workflows/phase5-qa.md` when starting this phase
- Validate documentation completeness
- Check cross-references
- Generate summary

---

## Core Architecture

### Design Principles

1. **Modularity**: Language-specific logic isolated in configuration sections
2. **Extensibility**: New languages and features added via configuration
3. **Progressive Analysis**: Incremental codebase analysis from high-level to code-level
4. **Progressive Loading**: Load files only as needed to save tokens
5. **Standards Compliance**: C4 model (all 4 levels), Mermaid diagrams
6. **Deep Code Analysis**: Function/class-level documentation like DeepWiki
7. **Navigable Structure**: Cross-referenced, searchable documentation

### Documentation Standards

- **Architecture Model**: C4 (Context, Container, Component, Code - all 4 levels)
- **Diagram Format**: Mermaid for all visualizations
- **Output Format**: Structured markdown with navigation in `./docs/`
- **Code Documentation**: Function/class-level API docs
- **Target Audience**: Product managers, architects, developers, DevOps engineers

### Enhanced Capabilities (DeepWiki-level)

- ✅ C4 Level 4 (Code) - Function/class documentation
- ✅ Automatic API reference generation
- ✅ Function call graphs
- ✅ Class inheritance diagrams
- ✅ Complexity analysis
- ✅ Code examples extraction
- ✅ Symbol cross-referencing
- ✅ Documentation index and navigation
- ✅ Test coverage documentation
- ✅ Performance considerations

---

## Quick Start Guide

When user requests documentation generation:

### Step 1: Language Detection
```markdown
Read file: .claude/skills/smart-docs/config/languages.md
→ Identify primary language(s) from file extensions
```

### Step 2: Language-Specific Setup
```markdown
Read file: .claude/skills/smart-docs/config/language-patterns/{detected-language}.md
→ Understand language-specific analysis patterns
```

### Step 3: Execute Phases Sequentially
```markdown
Phase 1: Read .claude/skills/smart-docs/workflows/phase1-discovery.md
         Execute discovery steps

Phase 2: Read .claude/skills/smart-docs/workflows/phase2-analysis.md
         Execute analysis steps

Phase 3: Read .claude/skills/smart-docs/workflows/phase3-generation.md
         For each document to generate:
           Read corresponding template from .claude/skills/smart-docs/templates/
           Generate document

Phase 4: Read .claude/skills/smart-docs/workflows/phase4-diagrams.md
         Create diagrams

Phase 5: Read .claude/skills/smart-docs/workflows/phase5-qa.md
         Validate and summarize
```

---

## Important Notes

### Token Efficiency

- **Do NOT** read all workflow and template files upfront
- **Do** read only the workflow file for the current phase
- **Do** read only the specific template when generating that document
- **Do** read only the language pattern for detected languages

### File Discovery Always Unlimited Depth

**Critical**: When discovering files, ALWAYS use unlimited depth:
- Visual display (tree): May be limited to `-L 3` for readability
- File discovery (Glob): Always use `**/*.ext` (unlimited depth)
- ALL files at ANY depth are discovered and analyzed

### Extension

To add a new language:
1. Add entry to `config/languages.md`
2. Create `config/language-patterns/{new-language}.md`
3. No changes needed to workflows or templates

To add a new template:
1. Create template file in appropriate `templates/` subdirectory
2. Reference it from `workflows/phase3-generation.md`

---

## Execution Summary

When you start documentation generation:

```
1. [READ] config/languages.md
2. [DETECT] Primary language(s)
3. [READ] config/language-patterns/{language}.md (for each detected language)
4. [READ] workflows/phase1-discovery.md
5. [EXECUTE] Phase 1
6. [READ] workflows/phase2-analysis.md
7. [EXECUTE] Phase 2
8. [READ] workflows/phase3-generation.md
9. [FOR EACH DOCUMENT]:
   - [READ] appropriate template from templates/
   - [GENERATE] document
10. [READ] workflows/phase4-diagrams.md
11. [EXECUTE] Phase 4
12. [READ] workflows/phase5-qa.md
13. [EXECUTE] Phase 5
14. [PRESENT] Summary
```

---

## Best Practices

### Before Generation
1. Clean build artifacts from project
2. Ensure README is up-to-date
3. Identify critical components

### During Generation
1. Follow progressive loading workflow
2. Read files only as needed
3. Monitor token usage
4. Save progress frequently

### After Generation
1. Review accuracy
2. Add domain-specific knowledge
3. Validate cross-references
4. Update diagrams if needed
5. Commit to version control

---

## Troubleshooting

**Issue**: "Cannot find workflow/template file"
- Ensure you're reading from correct path: `.claude/skills/smart-docs/{path}`
- Check file exists in skill directory

**Issue**: "Too much context used"
- Verify you're not reading all files upfront
- Read files progressively as documented

**Issue**: "Unknown language"
- Check if language pattern exists in `config/language-patterns/`
- Fall back to generic analysis if no specific pattern

---

**Version**: 2.0 (Modular, DeepWiki-Enhanced)  
**Last Updated**: 2025-01-15  
**Structure**: Progressive loading for token efficiency  
**Compatibility**: Claude Code, all mainstream languages  

---

*Now proceed to read `config/languages.md` to begin language detection*