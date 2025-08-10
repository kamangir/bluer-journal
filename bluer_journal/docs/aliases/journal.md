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
	[dryrun,~push,~sync,token]
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
	[dryrun] \
	[~pull,token] \
	[~push,token] \
	[--checklist 0] \
	[--relations 0] \
	[--verbose 1]
 . sync journal.
```
