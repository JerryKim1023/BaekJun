words = input().upper()   
setting_words = list(set(words))
# ex)ariranga    /   setting_words = aring    cnt_list = 3 2 1 1 1 
cnt_list = []
for i in setting_words:
    cnt = words.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(setting_words[max_index])