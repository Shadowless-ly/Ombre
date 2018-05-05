import re
import datetime

# # 识别后续字符串
# str_lst = ["bat", "bit", "but", "hat", "hit", "hut"]
# macth_word = re.compile("[bh][aiu]t", re.IGNORECASE)
# for i in str_lst:
#     if macth_word.match(i): print(macth_word.match(i).group())


date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date = "当前时间：" + date
print(date)
print(re.sub(r".*?(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+).*", r"\g<year>,\g<month>,\g<day>", date))