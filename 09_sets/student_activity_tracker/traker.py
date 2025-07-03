print("Students_Activity_Tracker 2025")
Criket = {"Alice", "Bob", "David", "Eve", "George", "Harry"}
Coding = {"Alice", "Charlie", "Eve", "Frank", "George", "Harry"}
Music = {"Alice", "Bob", "David", "George", }
in_criket_coding_music = Criket & Coding & Music

in_criket_coding = Criket & Coding 
in_coding_music = Coding & Music
in_music_criket = Criket & Music
in_exact_two_clubs = (in_criket_coding | in_coding_music | in_music_criket)-in_criket_coding_music

only_criket = Criket - Coding - Music
only_coding = Coding - Criket - Music
only_music = Music - Criket - Coding
only_1_club = only_criket | only_coding | only_music

print("Students in all 3 clubs:",in_criket_coding_music)
print("Students in exactly 2 clubs:",in_exact_two_clubs)
print("Students in only 1 club:", only_1_club)


