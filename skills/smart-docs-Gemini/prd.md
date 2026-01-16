# 产品需求文档 (PRD): Smart Docs - V3.0 (Final Release)

| 文档版本     | V3.0                                                     |
| :------- | :------------------------------------------------------- |
| **产品名称** | Smart Docs (AI-Powered Codebase Documentation Generator) |
| **状态**   | **已实现/生产就绪**                                             |
| **核心技术** | LLM Agent + **Tree-sitter Static Analysis**              |
| **目标**   | 为任意规模的代码仓（含10k+文件大仓）自动生成 **DeepWiki 级别** 的、概念导向的工程文档。    |

---

## 1. 产品概述

### 1.1 核心价值
解决传统工具生成的文档“只见树木不见森林”的问题。Smart Docs V3.0 不仅能生成精准的 API 手册，更能通过 AST 分析提取**核心概念、业务流程和架构图谱**，将冷冰冰的代码转换为具备业务语义的 DeepWiki 知识库。

### 1.2 关键差异化特性
1.  **精准无幻觉**：摒弃正则表达式，使用 **Tree-sitter** 解析 AST，100% 还原代码结构、继承关系和调用链。
2.  **大仓免疫 (Large Repo Immunity)**：通过“骨架扫描” (`tree -d`)、“精准定位” (`find`) 和“数据截断”技术，能够安全分析 10,000+ 文件、7层深度的超大仓库，永不爆 Context。
3.  **概念导向 (Concept-Oriented)**：文档结构不再是文件列表，而是按 **Core Concepts**、**Pipelines**、**Data Structures** 组织，符合人类认知习惯。
4.  **自我监控**：Agent 在每一步操作后都会执行 **Context Safety Check** 并汇报 Token 消耗，确保运行稳定。

---

## 2. 核心功能 (Functional Requirements)

### 2.1 全栈语言支持
*   **支持列表**：C, C++, Rust, Java, Go, JavaScript, TypeScript, Python, PHP。
*   **实现方式**：内置 9 套 Tree-sitter 查询语句 (`.scm`)，自动适配。

### 2.2 深度代码透视 (Deep Analysis)
通过 `analyze_code.py` 工具实现：
*   **符号提取**：Function/Method, Class/Interface, Docstrings。
*   **关系图谱**：
    *   **Calls**：函数内的调用关系（去重、归属到父函数）。
    *   **Extends**：类继承与接口实现关系。
    *   **Imports**：跨模块依赖关系。
*   **代码度量**：
    *   **Complexity**：计算圈复杂度 (Cyclomatic Complexity)。
    *   **LOC**：基于 AST 范围计算精准代码行数。

### 2.3 DeepWiki 文档体系
生成的文档结构 (`docs/`)：
*   **`core-concepts/`**：核心业务实体（如 "TransactionManager", "AgentModel"）。
*   **`pipelines/`**：关键处理流程（如 "Request Lifecycle", "Data Ingestion"）。
*   **`data-structures/`**：数据模型与配置字典（分离于行为逻辑之外）。
*   **`architecture/`**：C4 模型（Context, Container, Component, Code）。
*   **`api-reference/`**：详尽的技术参考手册。
*   **`reference/`**：复杂度报告、符号索引表、测试覆盖率。

### 2.4 动态可视化
*   基于 AST 数据自动生成 **Mermaid** 图表：
    *   Class Diagram (继承/组合)
    *   Call Graph (调用流)
    *   Sequence Diagram (关键交互)

---

## 3. 技术架构与安全机制

### 3.1 架构设计
*   **Perception (感知)**：Python Tool (`tools/analyze_code.py`) + Tree-sitter。负责“看”代码，输出客观 JSON。
*   **Cognition (认知)**：LLM Agent。负责“读”JSON，结合 README 理解业务意图，进行概念聚类。
*   **Action (执行)**：LLM Agent。负责组织 Markdown，绘制 Mermaid，写入文件。

### 3.2 大仓防御策略 (Large Repo Strategy)
这是 V3.0 的核心升级点：
1.  **Phase 1 Discovery**: 使用 `tree -d -L 7` 只看目录骨架，不看文件列表，节省 90% Token。
2.  **Phase 2 Analysis**:
    *   **Target Discovery**: 使用 `find` 命令按需查找文件，不依赖内存列表。
    *   **Sampling**: 对同构模块进行采样分析。
    *   **Truncation**: 工具层强制截断过长的 `calls` (>50) 和 `imports` (>100) 列表。
    *   **Batching**: 强制分批处理，处理完即丢弃原始 JSON，只保留“概念摘要”。

### 3.3 上下文监控 (Context Monitoring)
*   **Step-by-Step Reporting**: Agent 在每个操作步骤（Shell执行、文件读取）后，强制汇报当前 Context 使用量。
*   **Pre-flight Check**: 读取文件前必须先 `ls -lh`，超过 50KB 严禁直接 `Read`。

---

## 4. 执行流程 (Workflow Specification)

### Phase 1: Discovery
*   **目标**：建立项目骨架认知。
*   **关键动作**：`tree -d` (目录), `find ... config` (技术栈), `wc -l` (规模)。

### Phase 2: Analysis (The Engine)
*   **目标**：提取结构化数据 + 概念聚类。
*   **关键动作**：`find ... src` (找目标) -> `python analyze_code.py` (解析) -> **Concept Clustering** (归纳)。

### Phase 3: Generation
*   **目标**：写入文档。
*   **关键动作**：优先写 `Core Concepts`，最后写 `API Reference`。路径严格限定为 `docs/`。

### Phase 4: Diagrams
*   **目标**：可视化增强。
*   **关键动作**：基于 Phase 2 的关系数据，向 Markdown 中插入 Mermaid 代码块。

---

## 5. 验收标准 (Acceptance Criteria)

1.  **准确性**：生成的 API 列表必须与源代码实际签名一致（包括参数、返回值）。
2.  **关系正确性**：生成的类图必须正确反映 `extends/implements` 关系。
3.  **安全性**：在 10,000+ 文件仓库中运行，不应出现 Token Limit 错误。
4.  **可读性**：生成的 `index.md` 必须是业务导向的，而非文件列表导向。