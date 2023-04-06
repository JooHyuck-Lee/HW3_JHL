#!/usr/bin/env python
# coding: utf-8

# In[5]:


def reverse_words(str):
    word_list = list(str.split(" "))
    rev_list = word_list[::-1]
    str = ""
    for i in range(len(rev_list)):
        str = str + rev_list[i] + " "
        
    return str




def main():
    str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    rev_str1 = reverse_words(str1)
    print(rev_str1)
    
    str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same"
    rev_str2 = reverse_words(str2)
    print(rev_str2)

    
    
    
if __name__ == "__main__":
    main()


# In[ ]:




