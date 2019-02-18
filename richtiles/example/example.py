import richtiles
mylist = richtiles.get_tiles_by_extent(-180,-90,180,90, '/Volumes/Elements/university_of_bristol/js16170/data/merit/dem3_old/')
richtiles.write_tiles_layout(mylist,'myfile.txt')