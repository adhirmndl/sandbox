class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        sumA  = 0
        sumA2 = 0
        n     = 0
        for i in A:
            sumA  += i
            sumA2 += i*i
            n     += 1
        sumN  = n * (n + 1) / 2
        retA = sumN - sumA
        retB = (sumN * (2*n + 1)/3 - sumA2)/retA
        x = (retB - retA)/2
        return (x, x + retA)

    def repeatedNumberSucky(self, A):
        xor = 0
        for i in A:
            xor = xor ^ i
        for i in range(len(A)):
            xor = xor ^ (i+1)
        dSum = len(A) * (len(A)+1) / 2
        rSum = sum(A)
        diff = dSum - rSum
        pair = None
        for i in range(len(A)):
            if ((xor ^ (1 + i) ^ (1 + i + diff)) == 0):
                # the following line is shameful
                if not (i + 1 + diff) in A and (i + 1 + diff != 0):
                    pair = (i+1, i+1 + diff)
                    break
        return pair

s = Solution()
print s.repeatedNumber([4,1,2,5,4])
inp = [ 389, 299, 65, 518, 361, 103, 342, 406, 24, 79, 192, 181, 178, 205, 38, 298, 218, 143, 446, 324, 82, 41, 312, 166, 252, 59, 91, 6, 248, 395, 157, 332, 352, 57, 106, 246, 506, 261, 16, 470, 224, 228, 286, 121, 193, 241, 203, 36, 264, 234, 386, 471, 225, 466, 81, 58, 253, 468, 31, 197, 15, 282, 334, 171, 358, 209, 213, 158, 355, 243, 75, 411, 43, 485, 291, 270, 25, 100, 194, 476, 70, 402, 403, 109, 322, 421, 313, 239, 327, 238, 257, 433, 254, 328, 163, 436, 520, 437, 392, 199, 63, 482, 222, 500, 454, 84, 265, 508, 416, 141, 447, 258, 384, 138, 47, 156, 172, 319, 137, 62, 85, 154, 97, 18, 360, 244, 272, 93, 263, 262, 266, 290, 369, 357, 176, 317, 383, 333, 204, 56, 521, 502, 326, 353, 469, 455, 190, 393, 453, 314, 480, 189, 77, 129, 439, 139, 441, 443, 351, 528, 182, 101, 501, 425, 126, 231, 445, 155, 432, 418, 95, 375, 376, 60, 271, 74, 11, 419, 488, 486, 54, 460, 321, 341, 174, 408, 131, 115, 107, 134, 448, 532, 292, 289, 320, 14, 323, 61, 481, 371, 151, 385, 325, 472, 44, 335, 431, 187, 51, 88, 105, 145, 215, 122, 162, 458, 52, 496, 277, 362, 374, 26, 211, 452, 130, 346, 10, 315, 459, 92, 531, 467, 309, 34, 281, 478, 477, 136, 519, 196, 240, 12, 288, 302, 119, 356, 503, 527, 22, 27, 55, 343, 490, 127, 444, 308, 354, 278, 497, 191, 294, 117, 1, 396, 125, 148, 285, 509, 208, 382, 297, 405, 245, 5, 330, 311, 133, 274, 275, 118, 463, 504, 39, 99, 442, 337, 169, 140, 104, 373, 221, 499, 413, 124, 510, 159, 465, 80, 276, 83, 329, 524, 255, 387, 259, 397, 491, 517, 23, 4, 230, 48, 349, 412, 142, 114, 487, 381, 164, 35, 67, 498, 73, 440, 108, 226, 96, 132, 144, 207, 235, 33, 69, 128, 236, 364, 198, 475, 173, 493, 150, 90, 515, 111, 68, 232, 340, 112, 526, 492, 512, 495, 429, 146, 336, 17, 350, 251, 7, 184, 76, 380, 359, 293, 19, 49, 345, 227, 212, 430, 89, 474, 279, 201, 398, 347, 273, 37, 185, 177, 102, 304, 295, 422, 94, 426, 514, 116, 183, 180, 494, 42, 305, 152, 390, 30, 247, 451, 32, 388, 331, 78, 424, 368, 394, 188, 306, 449, 8, 214, 120, 179, 280, 511, 409, 338, 153, 507, 370, 461, 217, 161, 483, 147, 242, 86, 417, 268, 71, 462, 420, 167, 513, 379, 307, 522, 435, 113, 296, 457, 525, 45, 529, 423, 427, 2, 438, 64, 316, 46, 40, 13, 516, 367, 233, 110, 318, 250, 283, 216, 186, 310, 237, 377, 365, 175, 479, 378, 66, 414, 473, 165, 210, 50, 348, 372, 363, 339, 20, 168, 284, 415, 505, 206, 53, 223, 434, 202, 123, 399, 400, 135, 269, 428, 219, 456, 28, 464, 267, 489, 98, 391, 195, 366, 300, 484, 533, 229, 213, 149, 160, 256, 303, 530, 301, 29, 404, 344, 401, 220, 287, 9, 407, 170, 450, 523, 249, 72, 410, 3, 21, 200, 260 ]

print s.repeatedNumber(inp)

test2 = [ 119, 580, 468, 653, 687, 603, 32, 563, 510, 750, 566, 757, 74, 598, 426, 262, 561, 146, 554, 174, 547, 702, 227, 811, 767, 816, 565, 793, 377, 809, 379, 672, 409, 53, 661, 3, 382, 54, 85, 269, 612, 532, 108, 288, 716, 111, 407, 427, 82, 708, 798, 785, 617, 647, 310, 439, 366, 314, 384, 531, 78, 618, 57, 237, 548, 120, 38, 323, 654, 367, 65, 774, 626, 390, 614, 279, 562, 373, 188, 387, 270, 202, 308, 747, 813, 610, 167, 484, 664, 762, 2, 587, 18, 153, 4, 272, 234, 539, 475, 404,
        334, 110, 358, 481, 84, 143, 221, 501, 339, 317, 316, 671, 171, 578, 607, 662, 590, 311, 374, 689, 514, 302, 266, 611, 431, 751, 491, 703, 364, 555, 124, 341, 62, 429, 530, 560, 253, 186, 447, 745, 821, 71, 601, 526, 517, 370, 183, 309, 755, 609, 244, 226, 595, 333, 372, 721, 698, 87, 508, 814, 776, 200, 286, 696, 500, 648, 478, 717, 820, 630, 160, 179, 255, 635, 10, 59, 210, 670, 777, 6, 577, 738, 499, 283, 569, 697, 522, 749, 692, 496, 13, 403, 588, 285, 753, 586, 116, 224, 663,
        644, 378, 363, 731, 624, 667, 232, 732, 17, 381, 60, 486, 222, 45, 181, 240, 613, 589, 192, 542, 545, 806, 277, 219, 136, 95, 394, 280, 273, 267, 37, 786, 538, 261, 623, 768, 102, 293, 558, 421, 351, 335, 138, 238, 665, 681, 163, 435, 100, 352, 802, 92, 91, 140, 121, 29, 297, 164, 449, 39, 637, 342, 585, 209, 337, 290, 389, 551, 482, 764, 758, 735, 787, 461, 704, 105, 608, 52, 115, 822, 792, 109, 345, 55, 135, 794, 419, 685, 489, 512, 133, 728, 63, 393, 720, 433, 391, 112, 725,
        131, 567, 432, 591, 248, 1, 452, 11, 307, 9, 479, 161, 605, 28, 789, 130, 534, 368, 800, 295, 494, 638, 68, 483, 808, 23, 497, 249, 471, 763, 218, 64, 445, 162, 203, 296, 660, 19, 817, 771, 686, 754, 727, 619, 505, 406, 196, 688, 399, 795, 170, 247, 385, 75, 51, 129, 783, 519, 454, 450, 319, 43, 417, 719, 511, 301, 412, 97, 173, 354, 655, 199, 22, 651, 759, 773, 185, 674, 737, 746, 713, 442, 113, 744, 470, 276, 415, 594, 395, 495, 331, 176, 436, 677, 701, 801, 540, 462, 573, 93,
        402, 274, 465, 622, 782, 292, 328, 441, 418, 523, 48, 446, 805, 265, 67, 683, 77, 98, 158, 480, 788, 414, 175, 675, 405, 104, 504, 152, 668, 444, 205, 722, 583, 134, 658, 642, 21, 736, 684, 639, 168, 40, 251, 256, 305, 271, 521, 215, 50, 375, 492, 796, 190, 606, 516, 652, 313, 546, 733, 154, 303, 56, 106, 775, 592, 408, 217, 564, 712, 784, 597, 315, 524, 149, 434, 383, 70, 69, 460, 320, 259, 812, 502, 457, 230, 177, 356, 327, 695, 211, 518, 645, 574, 125, 549, 376, 254,
        453, 643, 355, 536, 593, 572, 646, 220, 107, 150, 34, 156, 137, 765, 770, 411, 734, 657, 467, 513, 326, 729, 122, 365, 278, 714, 507, 24, 241, 103, 343, 12, 633, 769, 214, 79, 707, 458, 503, 58, 26, 332, 818, 700, 401, 353, 194, 298, 599, 7, 634, 123, 225, 422, 144, 815, 743, 760, 304, 312, 602, 779, 459, 666, 73, 126, 324, 466, 711, 420, 94, 659, 506, 242, 359, 550, 208, 575, 201, 318, 676, 347, 142, 474, 191, 525, 437, 552, 49, 576, 649, 83, 151, 257, 509, 490, 456, 706, 371,
        101, 268, 430, 682, 61, 621, 400, 398, 299, 127, 386, 650, 463, 361, 740, 380, 726, 631, 615, 584, 807, 81, 264, 46, 33, 761, 473, 529, 742, 223, 741, 477, 351, 804, 423, 669, 157, 766, 694, 195, 5, 291, 699, 165, 184, 369, 488, 187, 438, 169, 197, 541, 346, 330, 396, 410, 88, 781, 582, 397, 772, 520, 132, 710, 159, 556, 182, 448, 80, 620, 544, 543, 636, 260, 155, 691, 258, 72, 568, 690, 235, 14, 243, 294, 141, 756, 748, 306, 281, 282, 656, 349, 799, 236, 485, 300, 321, 329, 493,
        30, 245, 229, 579, 739, 15, 360, 487, 89, 780, 515, 213, 797, 336, 27, 424, 233, 557, 8, 498, 357, 627, 678, 228, 36, 128, 20, 287, 206, 428, 275, 114, 25, 31, 596, 425, 413, 322, 693, 340, 570, 528, 246, 640, 99, 819, 724, 42, 790, 180, 193, 139, 680, 44, 616, 338, 148, 392, 600, 231, 451, 204, 535, 625, 216, 571, 632, 641, 66, 47, 440, 207, 388, 416, 718, 553, 147, 35, 527, 472, 730, 604, 791, 350, 348, 145, 263, 476, 362, 41, 469, 90, 166, 464, 289, 178, 673, 118, 325, 455, 679,
        778, 537, 250, 629, 172, 212, 803, 284, 715, 723, 533, 559, 709, 810, 581, 198, 344, 16, 252, 76, 752, 239, 117, 96, 443, 705, 189, 628 ]

print s.repeatedNumber(test2)