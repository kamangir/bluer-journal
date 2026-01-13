# aliases: journal

```bash
@journal \
	git \
	cd
 . cd git/journal.
@journal \
	git \
	pull \
	[~pull,token]
 . git -> journal.
@journal \
	git \
	push \
	[dryrun,~offline,~push,~sync,token]
 . journal -> git.
```

```bash
@journal \
	next \
	[<title>] \
	[~open] \
	[~offline,~push,token] \
	[--checklist 0] \
	[--relations 0] \
	[--sync 0]] \
	[--verbose 1]
 . create the next page.
```

```bash
@journal \
	open \
	[home | <YYYY-MM-DD>]
 . open journal.
```

```bash
@journal \
	sync \
	[dryrun,~offline] \
	[~pull,token] \
	[~offline,~push,token] \
	[--checklist 0] \
	[--relations 0] \
	[--verbose 1]
 . sync journal.
```
