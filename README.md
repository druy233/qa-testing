# qa-testing

软件测试练习工程：接口测试、UI 自动化、用例设计。

## 技术栈

- Python 3.12
- pytest（测试框架）
- requests（接口请求）
- Playwright / Selenium（UI 自动化，后续加入）

## 目录

```
qa-testing/
├─ tests/               # 测试用例
├─ week05-capture/      # 抓包与弱网分析
├─ week06-sql/          # SQL 练习
├─ week07-api/          # 接口测试
├─ week08-ui/           # UI 自动化
├─ pytest.ini
└─ README.md
```

## 运行

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt   # 或 pip install pytest requests
pytest -q
```

## 说明

- 用例覆盖：功能、边界、异常、弱网、兼容性
- 接口测试：requests + pytest，断言状态码与响应字段
- UI 自动化：Playwright，页面对象封装
