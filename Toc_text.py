#!/usr/bin/env python
# coding: utf-8

# In[1]:


def toc_text(text, tabulka, delka, offset=0):
    if delka==1:
        tabulka[offset][offset] = text[0]
        return
    if len(text) == 0:
        return
    
    i = 0
    # x sloupec
    # y radek
    for x in range(delka):
        tabulka[offset+0][offset+x] = text[i]
        i += 1 # i = i+1
    for y in range(1, delka-1):
        tabulka[offset+y][offset+delka-1] = text[i]
        i += 1
    for x in range(delka):
        tabulka[offset+delka-1][offset+delka-1-x] = text[i]
        i += 1
    for y in range(1, delka-1):
        tabulka[offset+delka-1-y][offset+0] = text[i]
        i += 1
        
    toc_text(text[i:], tabulka, delka-2, offset+1)


# In[2]:


velikost = 6
tabulka = [[[] for i in range(velikost)] for j in range(velikost)]
text = [i for i in range(velikost*velikost)]


# In[3]:


toc_text(text[::-1], tabulka, velikost, 0)


# In[4]:


tabulka

