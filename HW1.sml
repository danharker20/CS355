(*
NAME:       Daniel Harker
ID:         011513968
DATE:       25 Jan 19
ASSIGNMENT: CptS 355 HW1
*)


(*************************************************************************************************************)
(*** PROBLEM 1 ***)
(* part a *)
(* exists *)
(* returns true if x is in the list, else returns false *)
fun exists (x, lst) =

    let 
        fun main (x,[]) = false |
            main (x, lst) = 
                if x = hd lst then true     (* val equals head of list, return true*)
                else exists(x, tl lst);     (* val not equal to head of list, try function again with all but head of list*)
    
    in 
        main (x,lst)
    end;

(* part b *)
(*the type is ''a * ''a list -> bool because the type doesn't matter, so it could be int * int list, list * list list, bool * bool list, etc. The function will work for any matching types *)
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 2 ***)
(* listUnion *)
(* returns union of 2 lists, values should only appear once in list *)
fun listUnion lst1 lst2 = 

    let 
        fun exists (x,[]) = false |         (* exists function from problem 1 *)
            exists (x, lst) = 
                if x = hd lst then true               
                else exists(x, tl lst); 

        fun removeRepeats [] = [] |     (* function that removes repeats from a list *)
            removeRepeats L = 
                if exists ((hd L), (tl L)) then removeRepeats (tl L)       (* if there's a repeat, call function again without hd val, since we know there's a duplicate somewhere else in the list *)
                else (hd L)::(removeRepeats (tl L));                        (* call function with hd value attached, because it's the only copy in the list *)
        
        fun main [] [] = [] |
            main lst1 [] = removeRepeats lst1 |              (* lst2 is empty so just remove repeats from lst1 *)
            main [] lst2 = removeRepeats lst2 |              (* lst1 is empty so just remove repeats from lst2 *)
            main lst1 lst2 = removeRepeats (lst1@lst2);      (* append lst1 and lst2, then remove the repeats from that new list - note: wouldn't work without parethesis around the append part*)
    in
        main lst1 lst2
    end; 
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 3 ***)
(* replace *)
(* replace the x value in list with given new value, return edited list *)
fun replace n v L = 

    let
        fun lengthOfList [] = 0 |               (* calcualte length of list *)
            lengthOfList L = 
                1 + lengthOfList (tl L);        (* if not empty, add 1 and repeat with tl L *)

        fun main n v [] = [] |
            main n v L = 
                if n > (lengthOfList L) then L              (* if index is greater than length of list, return list because otherwise it's out of bounds *)
                else 
                    if (n=0) then v::(tl L)                 (* at desired index, replace val at that index with v *)
                    else (hd L)::(main (n-1) v (tl L));     (* not at desired index, so append hd L to function with n-1 *)

    in 
        main n v L
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 4 ***)
(* prereqFor *)
(* part a *)
fun prereqFor ([], courseInQuestion) = [] |
    prereqFor (((courseName, listofprereqs)::allCourses), courseInQuestion) = 

    let 
        fun exists (x,[]) = false |         (* exists function from problem 1 *)
            exists (x, lst) = 
                if x = hd lst then true                
                else exists(x, tl lst);

        fun main ([], courseInQuestion) = [] |
            main (((courseName, listofprereqs)::allCourses), courseInQuestion) = 
                if exists (courseInQuestion, listofprereqs) then courseName::(prereqFor (allCourses, courseInQuestion)) (* if courseInQuestion is in list of prereqs for that the coursename, append courseName to function with rest of courses *)
                else prereqFor (allCourses, courseInQuestion);          (* otherwise, don't append it and just call the function like in the line above *)

    in  
        main (((courseName, listofprereqs)::allCourses), courseInQuestion)
    end;

(* part b *)
(* the type is ('a * ''b list) list * ''b -> 'a list because the input list and courseInQuestion can be different, but not necessarily polymorphic, hence the 'a and ''b instead of ''a for everything *)
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 5 ***)
(* isPalindrome *)
(* returns true if palindrome, else return false *)
fun isPalindrome string = 

    let
        fun checkIsPal [] [] = true |
            checkIsPal exLst [] = true |       
            checkIsPal [] revexLst = true |
            checkIsPal exLst revexLst =
                if (hd exLst) = #" " then checkIsPal (tl exLst) revexLst             (* if a space is found in exLst, return tl of exLst *)
                else if (hd revexLst) = #" " then checkIsPal exLst (tl revexLst)     (* if a space is found in revexLst, return tl of revexLst *)
                else if (Char.toUpper (hd exLst)) = (Char.toUpper (hd revexLst)) then checkIsPal (tl exLst) (tl revexLst) (* if Char.toUpper of each hd char is equal, pass tl of each function *)
                else false;                                                           (* this means the hd of each lst is not equal, therfore false *)
              
        fun main string = 
            checkIsPal (explode string) (rev (explode string))  (* pass exploded string and reverse exploded string to checkIsPal *)

    in  
        main string
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 6 ***)
(* groupSumtoN *)
fun groupSumtoN N L =

    let 
        fun sumList [] = 0 |                 (* sum of ints in list *)
            sumList L = 
                (hd L) + (sumList (tl L));    (* continually add hd L *)

        fun reverse [] = [] |         (* reverse - helper function that reverses list *)
            reverse (x::rest) =
                reverse rest@[x];     (* basically just put x (the head) at the end *)

        fun innerList n inner [] = [inner] |                (* breaks up numbers into sub lists - these lists go into the original list*)
            innerList n inner (x::rest) = 
                if ((sumList inner) + x) > n then inner::(innerList n [x] rest)  (* if inner list sum + x is great than n, stop putting more vals in inner list and append inner list to subsequent inner lists *)
                else (innerList n (x::inner) rest)                              (* inner list sum + x is less than n, so append x to the inner list *)

        (*** map ***)
        (* apply function to every element in list *)
        fun map f [] = [] |
            map f (x::rest) = (f x)::map f rest;

        fun main N [] = [[]] |
            main N (x::rest) = 
                if N < 0 then [[]]         (* won't work if N < 0, so return empty list list *)
                else map reverse (innerList N [] (x::rest)); (* do this for everything in the list --> create inner lists of numbers adding up to no more than N *)
                                                             (* inner lists will be append in reverse order so they need to be reversed *)
    in
        main N L
    end;
(*************************************************************************************************************)



(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)


(* PROBLEM 1a TEST *)
fun existsTest () =
    
    let 
        val existsT1 = ((exists (1,[])) = false)
        val existsT2 = ((exists ("c",["b","c","z"])) = true)
        val existsT3 = ((exists ([1],[[1]])) = true)
        val existsT4 = ((exists (0,[1,2,3,4])) = false)
        val existsT5 = ((exists (1,[1,2,3,4])) = true)

    in 
        print ("\nexistsTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(existsT1) ^ "\n" ^
                " test2: " ^ Bool.toString(existsT2) ^ "\n" ^
                " test3: " ^ Bool.toString(existsT3) ^ "\n" ^
                " test4: " ^ Bool.toString(existsT4) ^ "\n" ^
                " test5: " ^ Bool.toString(existsT5) ^ "\n")
    end;

(* PROBLEM 2 TEST *)
fun listUnionTest () =

    let 
        val listUnionT1 = ((listUnion [1,3,4] [2,3,4,5]) = [1,2,3,4,5])
        val listUnionT2 = ((listUnion [1,1,2,3,3,3] [1,3,4,5]) = [2,1,3,4,5])
        val listUnionT3 = ((listUnion ["a","b","c"] ["b","b","d"]) = ["a","c","b","d"])
        val listUnionT4 = ((listUnion [[1,2,3], [4,5]] [[1,2,3], [5,6]]) = [[4,5],[1,2,3],[5,6]])
        val listUnionT5 = ((listUnion [1,1,2,2,3,3] []) = [1,2,3])

    in 
        print ("\nlistUnionTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(listUnionT1) ^ "\n" ^
                " test2: " ^ Bool.toString(listUnionT2) ^ "\n" ^
                " test3: " ^ Bool.toString(listUnionT3) ^ "\n" ^
                " test4: " ^ Bool.toString(listUnionT4) ^ "\n" ^
                " test5: " ^ Bool.toString(listUnionT5) ^ "\n") 
    end;


(* PROBLEM 3 TEST *)
fun replaceTest () = 

    let 
        val replaceT1 = ((replace 3 40 [1, 2, 3, 4, 5, 6]) = [1,2,3,40,5,6])
        val replaceT2 = ((replace 0 "X" ["a", "b", "c", "d"]) = ["X","b","c","d"])
        val replaceT3 = ((replace 4 false [true, false, true, true, true]) = [true,false,true,true,false])
        val replaceT4 = ((replace 5 100 [0,1,2,3,4]) = [0,1,2,3,4])
        val replaceT5 = ((replace 1 40 []) = [])

    in 
        print ("\nreplaceTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(replaceT1) ^ "\n" ^
                " test2: " ^ Bool.toString(replaceT2) ^ "\n" ^
                " test3: " ^ Bool.toString(replaceT3) ^ "\n" ^
                " test4: " ^ Bool.toString(replaceT4) ^ "\n" ^
                " test5: " ^ Bool.toString(replaceT5) ^ "\n") 
    end;


(* PROBLEM 4a TEST *)
fun prereqForTest () = 

    let 
        val prereqsList = 
            [("Cpts122" , ["CptS121"]),
            ("CptS132" , ["CptS131"]),
            ("CptS223" , ["CptS122", "MATH216"]),
            ("CptS233" , ["CptS132", "MATH216"]),
            ("CptS260" , ["CptS223", "CptS233"]),
            ("CptS315" , ["CptS223", "CptS233"]),
            ("CptS317" , ["CptS122", "CptS132", "MATH216"]),
            ("CptS321" , ["CptS223", "CptS233"]),
            ("CptS322" , ["CptS223","CptS233"]),
            ("CptS350" , ["CptS223","CptS233", "CptS317"]),
            ("CptS355" , ["CptS223"]),
            ("CptS360" , ["CptS223","CptS260"]),
            ("CptS370" , ["CptS233","CptS260"]),
            ("CptS427" , ["CptS223","CptS360", "CptS370", "MATH216", "EE234"])]

        val prereqForT1 = ((prereqFor (prereqsList,"CptS260")) = ["CptS360","CptS370"])
        val prereqForT2 = ((prereqFor (prereqsList,"CptS223")) = ["CptS260","CptS315","CptS321","CptS322","CptS350","CptS355","CptS360","CptS427"])
        val prereqForT3 = ((prereqFor (prereqsList,"CptS355")) = [])
        val prereqForT4 = ((prereqFor (prereqsList,"CptS121")) = ["Cpts122"])
        val prereqForT5 = ((prereqFor (prereqsList,"CptS131")) = ["CptS132"])
    
    in 
        print ("\nprereqForTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(prereqForT1) ^ "\n" ^
                " test2: " ^ Bool.toString(prereqForT2) ^ "\n" ^
                " test3: " ^ Bool.toString(prereqForT3) ^ "\n" ^
                " test4: " ^ Bool.toString(prereqForT4) ^ "\n" ^
                " test5: " ^ Bool.toString(prereqForT5) ^ "\n")
    end;

(* PROBLEM 5 TEST *)
fun isPalindromeTest () = 

    let 
        val isPalindromeT1 = ((isPalindrome "a01 02 2010A") = true)
        val isPalindromeT2 = ((isPalindrome "Doc note I dissent a fast never prevents a fatness I diet on cod") = true)
        val isPalindromeT3 = ((isPalindrome "r A cE C a r    ") = true)
        val isPalindromeT4 = ((isPalindrome "not a palindrome") = false)
        val isPalindromeT5 = ((isPalindrome "Yreka Bakery") = true)

    in
        print ("\nisPalindromeTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(isPalindromeT1) ^ "\n" ^
                " test2: " ^ Bool.toString(isPalindromeT2) ^ "\n" ^
                " test3: " ^ Bool.toString(isPalindromeT3) ^ "\n" ^
                " test4: " ^ Bool.toString(isPalindromeT4) ^ "\n" ^
                " test5: " ^ Bool.toString(isPalindromeT5) ^ "\n")
    end;

(* PROBLEM 6 TEST *)
fun groupSumtoNTest () = 

    let 
        val groupSumtoNT1 = ((groupSumtoN 15 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) = [[1,2,3,4,5],[6,7],[8],[9],[10]])
        val groupSumtoNT2 = ((groupSumtoN 11 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) = [[1,2,3,4],[5,6],[7],[8],[9],[10]])
        val groupSumtoNT3 = ((groupSumtoN 1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
        val groupSumtoNT4 = ((groupSumtoN 0 [0,0,0,0,1,2,0,0]) = [[0,0,0,0],[1],[2],[0,0]])
        val groupSumtoNT5 = ((groupSumtoN 100 [1,2,3,4,5,6,7,8,9, 10]) = [[1,2,3,4,5,6,7,8,9,10]])

    in 
        print ("\ngroupSumtoNTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(groupSumtoNT1) ^ "\n" ^
                " test2: " ^ Bool.toString(groupSumtoNT2) ^ "\n" ^
                " test3: " ^ Bool.toString(groupSumtoNT3) ^ "\n" ^
                " test4: " ^ Bool.toString(groupSumtoNT4) ^ "\n" ^
                " test5: " ^ Bool.toString(groupSumtoNT5) ^ "\n")
    end;




(* RUN ALL TESTS *)

val _ = existsTest ();
val _ = listUnionTest ();
val _ = replaceTest ();
val _ = prereqForTest ();
val _ = isPalindromeTest ();
val _ = groupSumtoNTest ();