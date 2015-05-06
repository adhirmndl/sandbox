doubleMe x = x + x
doubleUs x y = x*2 + y*2

lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

charName :: Char -> String
charName 'a' = "Albert"
charName 'b' = "Broseph"
charName 'c' = "Cecil"

head' :: [a] -> a
head' [] = error "empty list"
head' (x:_) = x

take3 :: [a] -> [a]
take3 [] = error "empty list"
take3 (x:y:z:_) = [x,y,z]

length' :: (Num a) => [a] -> a
length' [] = 0
length' (_ : xs) = 1 + length' xs

--sum' :: (Num b) => [a] -> a
sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x : xs) = x + sum' xs
