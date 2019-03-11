authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")

author_last_names = []

for author in author_names:
  author_list = author.split()
  author_last_names.append(author_list[-1])
  
print(author_last_names)
  
  