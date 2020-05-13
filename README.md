# apiperms

Edit configuration.py to match your environment and specify your project
skeleton.

Use setroot.py on your Projects directory path to set the top-level ACLs.

Then use mktree.py to create a skeleton.

```
(apiperms) mbottMBP:apiperms mbott$ python setroot.py /Projects
(apiperms) mbottMBP:apiperms mbott$ python mktree.py -r /Projects -n Show01
(apiperms) mbottMBP:apiperms mbott$
```