
# class Reverse(object):
#     def refersee(self, s):
#         s[:] = s[::-1]
#         print(s)

# r = Reverse()
# r.refersee(s)




class string(object):
    def reverse(self,s):
        n =int(len(s))
        l = 0
        r = n-1
        temp = 0

        while(l<r):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l = l+1
            r = r-1
        print(s)

s = ["H", "a", "n", "n", "a", "h"]
string().reverse(s)


