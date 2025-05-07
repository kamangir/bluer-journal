# 📜 bluer-journal

📜 `@journal` with command access maintained in a github repo.  

```mermaid
graph LR

    journal_git_cd["@journal git cd"]

    journal_git_pull["@journal git pull"]

    journal_git_push["@journal git push"]

    journal_open["@journal open"]

    journal["📜 journal"]:::folder
    git["🗄️ git"]:::folder

    journal_git_cd --> git

    git --> journal_git_pull
    journal_git_pull --> journal

    journal --> journal_git_push
    journal_git_push --> git

    journal_open --> git

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

---

> 📜 For the [Global South](https://github.com/kamangir/bluer-south).

---

signature:::