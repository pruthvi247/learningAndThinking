![[Pasted image 20260202142018.png]]
Git has two layers:

1. Porcelain (user-facing commands): add, commit, checkout, rebase, etc.
    
2. Plumbing (low-level building blocks): hash-object, cat-file, read-tree, update-index, and more.
    

When you trigger a Git command:

1. Your porcelain command is translated by Git
    
2. It calls lower-level plumbing operations
    
3. Plumbing writes directly into the .git directory (Git’s entire internal database)
    

Inside the .git directory: Git stores everything it needs to reconstruct your repo.

- objects/ : all file content and metadata stored by hash
    
- refs/ : branches and tags
    
- index : staging area
    
- config : repo configuration
    
- HEAD : current branch pointer
    

The .git folder is your repository. If you delete it, the project loses its entire history.

Everything in Git is built from just four objects:

- blob : file contents
    
- tree : directories
    
- commit : metadata + parents
    
- tag : annotated reference
    

Over to you: Which Git command has confused you the most in real-world projects?
