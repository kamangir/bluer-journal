# aliases: journal

## git

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

## open

```bash
@journal \
	open \
	[home | <YYYY-MM-DD>]
 . open journal.
```

## sync

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
