#Recursive function
def TowerOfHanoi(n , source_rod="Silver", dest_rod="Golden", temp_rod="Bronze"):

    if n == 1:
    #moves final remaining disk from source to dest
        print ("Move disk 1 from rod",source_rod,"to rod",dest_rod)
        return 
        
    #moves disks from source to temp using dest
    TowerOfHanoi(n-1, source_rod, temp_rod, dest_rod)
    
    #moves disk from source to dest directly
    print ("Move disk",n,"from rod",source_rod,"to rod",dest_rod)
    
    #moves disks from temp to dest using source
    TowerOfHanoi(n-1, temp_rod, dest_rod, source_rod)

        
#Main Call
TowerOfHanoi (int(input('Enter the no of disks:\n')))
