r=replicate
t c 0 _=[]
t c s o=((r s ' ')++(r o c)):t 'o' (s-1) (o+2)
m = putStrLn $ (unlines) $(t '*' 10 1)

-- produces:
--           *          
--          ooo         
--         ooooo        
--        ooooooo       
--       ooooooooo      
--      ooooooooooo     
--     ooooooooooooo    
--    ooooooooooooooo   
--   ooooooooooooooooo  
--  ooooooooooooooooooo 
