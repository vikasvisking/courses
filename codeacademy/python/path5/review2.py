highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems + '\n')

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

highlighted_poems_stripped = []
for element in highlighted_poems_list:
  char = element.strip()
  highlighted_poems_stripped.append(char)
  
print(highlighted_poems_stripped)

highlighted_poems_details = []

for chars in highlighted_poems_stripped:
  char = chars.split(":")
  highlighted_poems_details.append(char)
  
print(highlighted_poems_details)
  
titles = []
poets = []
dates = []

for poems in highlighted_poems_details:
  title = poems[0]
  poet = poems[1]
  date = poems[2]
  titles.append(title)
  poets.append(poet)
  dates.append(date)
  
for i in range(len(titles)):
  string = "The poem {title} was published by {poet} in {date}".format(title = titles[i], poet = poets[i], date= dates[i])
  print(string)
  
  
  
  

  