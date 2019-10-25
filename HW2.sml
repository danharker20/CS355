(*
NAME:       Daniel Harker
ID:         011513968
DATE:       12 Feb 19
ASSIGNMENT: CptS 355 HW2
*)

(*************************************************************************************************************)
(*** fold ***)
fun fold f base [] = base |
    fold f base (x::rest) = f x (fold f base rest);

(*** map ***)
fun map f [] = [] |
    map f (x::rest) = (f x)::map f rest;

(*** filter ***)
fun filter pred [] = [] |
    filter pred (x::rest) = 
        if pred x then x::(filter pred rest)
        else (filter pred rest);
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 1 ***)
(* part a *)
(* merge2 *)
(* merges 2 sorted lists into 1 sorted list *)
fun merge2 lst1 lst2 = 

    let
        fun main [] [] = [] |
            main lst1 [] = lst1 |
            main [] lst2 = lst2 |             
            main lst1 lst2 = 
                if (hd lst1) <= (hd lst2) then (hd lst1)::(main (tl lst1) lst2) (* cons hd lst1 to rest of lists *)
                else (hd lst2)::(main lst1 (tl lst2)); (* cons hd lst2 to rest of lists *)
    in
        main lst1 lst2
    end;

(* part b *) 
(* merge2Tail *)
(* merges 2 sorted lists into 1 sorted lists *)
fun merge2Tail lst1 lst2 = 

    let 
        fun revAppend [] L = L |                             (* taken from slides *)
            revAppend (x::rest) L = revAppend rest(x::L);       

        fun main [] [] acc = [] |
            main lst1 [] acc = revAppend acc lst1 |
            main [] lst2 acc = revAppend acc lst2 |
            main (x::restX) (y::restY) acc = 
                if x > y then main (x::restX) restY (y::acc) (* append smaller value to list, making list of numbers larger to smaller *)   
                else main restX (y::restY) (x::acc);
    in
        main lst1 lst2 []
    end;

(* part c *)
(* mergeN *)
(* use fold *)
(* merges list of sorted lists into a sorted list *)
fun mergeN L = 

    let 
        fun main [] = [] |
            main L = 
                fold merge2 [] L; (* fold func-->merge2 base-->[] list-->L *)
    in
        main L
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 2 ***)
(* part a *)
(* getInRange *)
(* returns values in list that are between v1 and v2 exclusively *)
fun getInRange v1 v2 L =

    let
        fun main v1 v2 [] = [] |
            main v1 v2 L = 
                filter (fn x=> x>v1 andalso x<v2) L
                (* filter numbers in list between v1 and v2 *)
    in
        main v1 v2 L
    end;

(* part b *)
(* countInRange *)
(* returns number of values in list of lists that are between v1 and v2 exclusively *)
fun countInRange v1 v2 L = 

    let 
        fun main v1 v2 [] = 0 |
            main v1 v2 L = 
                fold (fn x=> fn y=> x+y) 0 (map (fn x=> x-x+1) (getInRange v1 v2 (fold (fn x=> fn y=> x@y) [] L)));
                (* fold the list of lists into 1 list *)
                (* get numbers in range v1 and v2 exclusively *)
                (* change the number to 1 *)
                (* add all numbers in list --> gives desired total *)
    in
        main v1 v2 L
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 3 ***)
(* part a *)
(* addLengths *)
(* returns 2 lengthUnits added together in the form of INCH x *)
datatype lengthUnit = INCH of int | FOOT of int | YARD of int 

fun addLengths (length1) (length2) = 

    let
        fun changeToInch (INCH x) (INCH y) = INCH (x+y) |           
            changeToInch (INCH x) (FOOT y) = INCH (x+(12*y)) |
            changeToInch (INCH x) (YARD y) = INCH (x+(36*y)) |
            changeToInch (FOOT x) (INCH y) = INCH ((12*x)+y) |
            changeToInch (FOOT x) (FOOT y) = INCH ((12*x)+(12*y)) |
            changeToInch (FOOT x) (YARD y) = INCH ((12*x)+(36*y)) |
            changeToInch (YARD x) (INCH y) = INCH ((36*x)+y) |
            changeToInch (YARD x) (FOOT y) = INCH ((36*x)+(12*y)) |
            changeToInch (YARD x) (YARD y) = INCH ((36*x)+(36*y));      (* function converts any inch/foot/yard combo into all in inch *)

        fun main (length1) (length2) = 
            changeToInch (length1) (length2);
    in
        main (length1) (length2)
    end;

(* part b *)
(* addAllLengths *)
(* returns lengthUnits added together from list of lists in the form of INCH x *)
fun addAllLengths L = 

    let
        fun changeToInch (INCH x) (INCH y) = INCH (x+y) |
            changeToInch (INCH x) (FOOT y) = INCH (x+(12*y)) |
            changeToInch (INCH x) (YARD y) = INCH (x+(36*y)) |
            changeToInch (FOOT x) (INCH y) = INCH ((12*x)+y) |
            changeToInch (FOOT x) (FOOT y) = INCH ((12*x)+(12*y)) |
            changeToInch (FOOT x) (YARD y) = INCH ((12*x)+(36*y)) |
            changeToInch (YARD x) (INCH y) = INCH ((36*x)+y) |
            changeToInch (YARD x) (FOOT y) = INCH ((36*x)+(12*y)) |
            changeToInch (YARD x) (YARD y) = INCH ((36*x)+(36*y));       (* converts any inch/food/yard combo into all inch *)

        fun main [] = INCH 0 | 
            main L = 
                fold changeToInch (INCH 0) (fold (fn x=> fn y=> x@y) [] L);     (* fold the folded list of all measurments with addition*)
    in
        main L
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 4 ***)
(* part a *)
(* sumTree *)
datatype 'a Tree = LEAF of 'a | NODE of 'a * ('a Tree) * ('a Tree);
Control.Print.printDepth := 100;

(* sum of tree4 is 117*)
val tree4 = NODE(3, NODE(1, LEAF 5, NODE(0, LEAF 5, NODE(3, LEAF 2, LEAF 10))), NODE(5, NODE(2, LEAF 2, LEAF 3), LEAF 90));

fun sumTree T = 

    let
        fun main (LEAF v) = v |
            main (NODE (_, left, right)) = 
                (main left) + (main right)
    in
        main T
    end;

(* part b *)
(* createSumTree *)
(* returns: NODE (117, NODE (22,LEAF 5,NODE (17,LEAF 5,NODE (12,LEAF 2,LEAF 10))), NODE (95,NODE (5,LEAF 2,LEAF 3),LEAF 90)) *)
fun createSumTree T = 

    let
        fun sumTreeHelper (LEAF v) = v |
            sumTreeHelper (NODE (_, left, right)) = 
                (sumTreeHelper left) + (sumTreeHelper right)

        fun main (LEAF v) = (LEAF v) |
            main (NODE (_, left, right)) = 
                (NODE (((sumTreeHelper left)+(sumTreeHelper right)), (main left), (main right)))
    in
        main T
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*** PROBLEM 5 ***)
(* foldListTree *)
(* folds the listLEAFs of a listTree together *)
(* needs type: ('a -> 'a -> 'a) -> 'a -> 'a listTree -> 'a *)
datatype 'a listTree = listLEAF of ('a list) | listNODE of ('a listTree list);
Control.Print.printDepth := 100;

(* sum tree5 is 78 *)
(* mul tree5 is 479001600 *)
val tree5 = listNODE(
            [listNODE([listLEAF [1,2,3]]), 
            listNODE([listNODE([listLEAF [4,5,6,7,8], listLEAF [9]]), listLEAF []]), 
            listNODE([listLEAF [10], listLEAF [11]]),
            listLEAF [12]]);

(* functions to pass in as f *)
fun add x y = x+y;
fun mul x y = x*y;

fun foldListTree f base t = 

    let             
        fun main f base (listLEAF v) = (fold f base v) |
            main f base (listNODE x) = 
                fold f base (map (main f base) x);
    in
        main f base t
    end;
(*************************************************************************************************************)


(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)
(*************************************************************************************************************)

(* PROBLEM 1a TEST *)
fun merge2Test () =
    
    let 
        val merge2T1 = ((merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]) = [1,2,3,4,5,5,6,7,8,8,9,10])
        val merge2T2 = ((merge2 [1,2] [0,10,12]) = [0,1,2,10,12])
        val merge2T3 = ((merge2 [1,3,3,5,5] [~1,2,4]) = [~1,1,2,3,3,4,5,5])
        val merge2T4 = ((merge2 [] [~1,0,1,2,3]) = [~1,0,1,2,3])
        val merge2T5 = ((merge2 [1,2,3,4,5] [1,2,3,4,5]) = [1,1,2,2,3,3,4,4,5,5])

    in 
        print ("\nmerge2Test:-------------------- \n" ^
                " test1: " ^ Bool.toString(merge2T1) ^ "\n" ^
                " test2: " ^ Bool.toString(merge2T2) ^ "\n" ^
                " test3: " ^ Bool.toString(merge2T3) ^ "\n" ^
                " test4: " ^ Bool.toString(merge2T4) ^ "\n" ^
                " test5: " ^ Bool.toString(merge2T5) ^ "\n")
    end;

(* PROBLEM 1b TEST *)
fun merge2TailTest () =
    
    let 
        val merge2TailT1 = ((merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]) = [1,2,3,4,5,5,6,7,8,8,9,10])
        val merge2TailT2 = ((merge2Tail [1,2] [0,10,12]) = [0,1,2,10,12])
        val merge2TailT3 = ((merge2Tail [1,3,3,5,5] [~1,2,4]) = [~1,1,2,3,3,4,5,5])
        val merge2TailT4 = ((merge2Tail [] [~1,0,1,2,3]) = [~1,0,1,2,3])
        val merge2TailT5 = ((merge2Tail [1,2,3,4,5] [1,2,3,4,5]) = [1,1,2,2,3,3,4,4,5,5])

    in 
        print ("\nmerge2TailTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(merge2TailT1) ^ "\n" ^
                " test2: " ^ Bool.toString(merge2TailT2) ^ "\n" ^
                " test3: " ^ Bool.toString(merge2TailT3) ^ "\n" ^
                " test4: " ^ Bool.toString(merge2TailT4) ^ "\n" ^
                " test5: " ^ Bool.toString(merge2TailT5) ^ "\n")
    end;

(* PROBLEM 1c TEST *)
fun mergeNTest () =
    
    let 
        val mergeNT1 = ((mergeN [[1,2],[10,12],[2,5,6,8,9]]) = [1,2,2,5,6,8,9,10,12])
        val mergeNT2 = ((mergeN [[3,4],[~3,~2,~1],[1,2,5,8,9]]) = [~3,~2,~1,1,2,3,4,5,8,9])
        val mergeNT3 = ((mergeN [[1,2,3,4,5],[],[0],[2],[]]) = [0,1,2,2,3,4,5])
        val mergeNT4 = ((mergeN [[5],[4],[3],[2],[1],[0]]) = [0,1,2,3,4,5])
        val mergeNT5 = ((mergeN [[],[],[],[],[]]) = [])

    in 
        print ("\nmergeNTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(mergeNT1) ^ "\n" ^
                " test2: " ^ Bool.toString(mergeNT2) ^ "\n" ^
                " test3: " ^ Bool.toString(mergeNT3) ^ "\n" ^
                " test4: " ^ Bool.toString(mergeNT4) ^ "\n" ^
                " test5: " ^ Bool.toString(mergeNT5) ^ "\n")
    end;

(* PROBLEM 2a TEST *)
fun getInRangeTest () =
    
    let 
        val getInRangeT1 = ((getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11]) = [4,5,6,7,8,9])
        val getInRangeT2 = ((getInRange ~5 5 [~10,~5,0,5,10]) = [0])
        val getInRangeT3 = ((getInRange ~1 1 [~2,2,3,4,5]) = [])
        val getInRangeT4 = ((getInRange 0 1 [0,0,0,0,1,1,1,1,1]) = [])
        val getInRangeT5 = ((getInRange 0 2 [0,0,0,0,1,1,1,1,1]) = [1,1,1,1,1])

    in 
        print ("\ngetInRangeTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(getInRangeT1) ^ "\n" ^
                " test2: " ^ Bool.toString(getInRangeT2) ^ "\n" ^
                " test3: " ^ Bool.toString(getInRangeT3) ^ "\n" ^
                " test4: " ^ Bool.toString(getInRangeT4) ^ "\n" ^
                " test5: " ^ Bool.toString(getInRangeT5) ^ "\n")
    end;

(* PROBLEM 2b TEST *)
fun countInRangeTest () =
    
    let 
        val countInRangeT1 = ((countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]) = 6)
        val countInRangeT2 = ((countInRange ~5 5 [[~10,~5,~4],[0,4,5],[],[10]]) = 3)
        val countInRangeT3 = ((countInRange 1 5 [[1,5],[1],[5],[]]) = 0)
        val countInRangeT4 = ((countInRange 0 5 [[0],[1,3,4],[6,7,10]]) = 3)
        val countInRangeT5 = ((countInRange 0 10 [[],[1],[4,5,5,6],[],[],[9,9,10]]) = 7)

    in 
        print ("\ncountInRangeTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(countInRangeT1) ^ "\n" ^
                " test2: " ^ Bool.toString(countInRangeT2) ^ "\n" ^
                " test3: " ^ Bool.toString(countInRangeT3) ^ "\n" ^
                " test4: " ^ Bool.toString(countInRangeT4) ^ "\n" ^
                " test5: " ^ Bool.toString(countInRangeT5) ^ "\n")
    end;

(* PROBLEM 3a TEST *)
fun addLengthsTest () =
    
    let 
        val addLengthsT1 = ((addLengths (FOOT 2) (INCH 5)) = INCH 29)
        val addLengthsT2 = ((addLengths (YARD 3) (INCH 3)) = INCH 111)
        val addLengthsT3 = ((addLengths (FOOT 3) (FOOT 5)) = INCH 96)
        val addLengthsT4 = ((addLengths (YARD 90) (YARD 90)) = INCH 6480)
        val addLengthsT5 = ((addLengths (INCH 90) (INCH 0)) = INCH 90)

    in 
        print ("\naddLengthsTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(addLengthsT1) ^ "\n" ^
                " test2: " ^ Bool.toString(addLengthsT2) ^ "\n" ^
                " test3: " ^ Bool.toString(addLengthsT3) ^ "\n" ^
                " test4: " ^ Bool.toString(addLengthsT4) ^ "\n" ^
                " test5: " ^ Bool.toString(addLengthsT5) ^ "\n")
    end;

(* PROBLEM 3b TEST *)
fun addAllLengthsTest () =
    
    let 
        val addAllLengthsT1 = ((addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]) = INCH 262)
        val addAllLengthsT2 = ((addAllLengths [[FOOT 2], [FOOT 2, INCH 2],[]]) = INCH 50)
        val addAllLengthsT3 = ((addAllLengths []) = INCH 0)
        val addAllLengthsT4 = ((addAllLengths [[INCH 50,FOOT 9],[YARD 0, INCH ~50],[FOOT ~9]]) = INCH 0)
        val addAllLengthsT5 = ((addAllLengths [[],[INCH 5],[FOOT 20],[YARD 20]]) = INCH 965)

    in 
        print ("\naddAllLengthsTest:-------------------- \n" ^
                " test1: " ^ Bool.toString(addAllLengthsT1) ^ "\n" ^
                " test2: " ^ Bool.toString(addAllLengthsT2) ^ "\n" ^
                " test3: " ^ Bool.toString(addAllLengthsT3) ^ "\n" ^
                " test4: " ^ Bool.toString(addAllLengthsT4) ^ "\n" ^
                " test5: " ^ Bool.toString(addAllLengthsT5) ^ "\n")
    end;


(* RUN ALL TESTS *)
val _ = merge2Test ();
val _ = merge2TailTest ();
val _ = mergeNTest ();
val _ = getInRangeTest ();
val _ = countInRangeTest ();
val _ = addLengthsTest ();
val _ = addAllLengthsTest();





