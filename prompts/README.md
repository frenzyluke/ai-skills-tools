# AI 開發輔助腳本工具集 (AI Skills Tools)

本資料夾收錄了一系列基於 Gemini CLI 的 Bash 腳本，旨在透過預設的專業 Prompt，協助工程師快速進行程式碼審查、日誌分析、問題診斷及工程變更紀錄生成。

## 🛠️ 工具清單與說明

### 1. 邏輯分析與諮詢 (Logic & Problem Solving)
- **`ask-logic`**: 針對特定的邏輯問題進行分析。
  - **用法**: `ask-logic "描述你的問題"`
  - **分析重點**: 期望行為、實際行為、邏輯斷層 (Logic Gap Analysis)、根本原因、驗證方式及修復建議。
- **`logic-debug`**: 針對程式碼文件的邏輯漏洞進行深度分析。
  - **用法**: `logic-debug <file_path>`
  - **核心檢查點**: 條件判斷是否漏 case、流程順序、狀態切換、邊界條件。

### 2. 日誌與錯誤診斷 (Debugging & Logs)
- **`log-debug` / `py-error`**: 通用的系統與 Python 錯誤日誌分析工具。
  - **用法**: `log-debug <log_file>`
  - **分析重點**: 問題摘要、根本原因排序 (由高到低)、具體驗證指令、修復建議 (含 Workaround 與正式解)、風險與注意事項。
- **`mongo-debug`**: MongoDB 效能與查詢優化專家。
  - **用法**: `mongo-debug <file_or_log>`
  - **分析重點**: 問題類型 (Connection / Query / Index / Timeout)、索引建議 (Index Suggestion)、Python 實作範例。
- **`ops-debug`**: 熟悉 Docker、Linux、網絡與部署層級的錯誤分析。
  - **用法**: `ops-debug <log_file>`
  - **分析重點**: 判斷錯誤層級 (OS / Docker / Network / App / Permission)、提供可直接執行的除錯指令 (Debug Commands)。

### 3. 開發流程與變更紀錄 (Development Workflow)
- **`code-review`**: 針對指定檔案進行專業的程式碼審查。
  - **用法**: `code-review <file_path>`
  - **審查目標**: 降低認知複雜度 (Cognitive Complexity)、提升可維護性、檢查 Bug 與效能。
- **`change-log`**: 根據手動輸入的描述生成標準化的變更紀錄。
  - **用法**: `change-log "描述變更內容"`
- **`change-log-diff`**: 直接從 `git diff` 生成專業且深度的工程變更紀錄。
  - **用法**: `git diff | change-log-diff`
  - **分析重點**: 背景脈絡、修改重點、採用此方案的原因、系統影響、預期改善結果。

## 🚀 技術背景與專業領域
這些腳本專為以下技術棧與系統開發：
- **語言**: Python, C++, Bash
- **框架與數據庫**: FastAPI, MongoDB
- **基礎設施**: Docker, Linux, Network, Deployment
- **領域應用**: AOI (Automated Optical Inspection) 系統

## 📖 使用須知
- 所有腳本均依賴於 `gemini` CLI 工具，請確保環境中已正確安裝並設定 `gemini`。
- 腳本透過 `#!/usr/bin/env bash` 執行，建議將此資料夾加入 `PATH` 以便在任何路徑下使用。
