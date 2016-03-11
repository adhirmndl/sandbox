-- problem 1 : find last element of a list
myLast []     = error "empty!" 
myLast [x]    = x
myLast (_:xs) = myLast xs

-- problem 2 : find last but one element of a list
myButLast []     = error "empty!"
myButLast [x]    = error "too few!"
myButLast (x:xs) =
                if length xs == 1
                then x
                else myButLast xs

myButLast' x = reverse x !! 1

-- problem 3 : kth element in a list
elementAt (x:_)  1 = x
elementAt []     _ = error "out of bounds"
elementAt (_:xs) k
    | k < 1        = error "out of bounds" -- shortcut negative case
    | otherwise    = elementAt xs (k-1)

elementAt' x k = x !! (k - 1)

-- problem 4 : number of elements of a list
myLength []     = 0
myLength (_:xs) = 1 + myLength xs

-- accumulator
myLength' xs  = acc xs 0
        where
                acc []     n = n
                acc (_:xs) n = acc xs (n+1)

-- mapper
myLength'' = sum . map (\_->1)

-- foldl #TODO why doesn't this work?
-- myLength''' = foldl (\n _ -> n + 1) 0

-- problem 5 : reverse a list
myReverse xs = acc xs []
        where
                acc [] reversed = reversed
                acc (x:xs) reversed = acc xs (x:reversed)

-- problem 6 : palindrome
isPalindrome xs = p [] xs xs
        where
                p rev (x:xs) (_:_:ys) = p (x:rev) xs ys
                p rev (x:xs) [_]      = rev == xs
                p rev xs     []       = rev == xs

-- problem 7 : flatten nested list

data NestedList a = Elem a | List [NestedList a]

flatten (Elem x) = [x]
flatten (List (x:xs)) = flatten x ++ flatten (List xs)
flatten (List []) = []

-- problem 8 : eliminate consecutive duplicates
compress list = compress_acc list []
    where
        compress_acc []     acc = acc
        compress_acc [x]    acc = (acc ++ [x])
        cmopress_acc (x:xs) acc
            | x == (head xs)    = compress_acc xs acc
            | otherwise         = compress_acc xs (acc ++ [x])
