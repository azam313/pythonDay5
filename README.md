<h1><u>Lists in Pyyhon</u></h1>
<h3>A built-in data type that stores set of values</h3>
<h3>It can store elements of different types (integer,float,string,etc.</h3>
<p>marks = [87,64,33,95,76]   #marks[0],marks[1].. 
<p>student = ["Karan",85,"Delhi"]  #student[0], student[1].. </p>
<p>student[0] = "Arjun"  #allowed in python  </p>
<p>len(student)  #returns length </p>
<hr>

<h1><u>List Slicing</u></h1>
<h3>similar to String Slicing</h3>
<p>list_name[ starting_idx: ending_idx</p>
<p>marks = [87,64,33,95,76]</p>
<p>marks[1:4] is [64,33,95]</p>
<p>marks[1:] is same as marks[0:4]</p>
<p>marks[-3:-1] is [33,95]</p>
<hr>

<h1><u>List Method</u></h1>
<p>list = [2,1,3]</p>
<p>list.append(4)    #adds one elementy at the end</p>
<p>list.sort()       #sort in ascending order [1,2,3]</p>
<p>list.sort(reverse = True)     #sort in descending order [3,2,1]</p>
<p>list.reverce()    #reverses list [3,1,2]</p>
<p>list.insert(idx,el)      #insert element at index</p>
<p>list.remove(1)     #remove first occurrence of element [2,3,1]</p>
<p>list.pop(idx)     #removes elememnt at idx</p>
<hr>

<h1><u>Tuples in Python</u></h1>
<h3>A built-in data type lets us create immutable sequences of values.</h3>
<p>tup = (87,64,33,95,76)     #tup[0],tup[1]..</p>
<p>tup[0] = 43    #not allowed in python</p>
<p>tup1 = ()</p>
<p>tup2 = (1,)</p>
<p>tup3 = (1,2,3)</p>
<hr>

<h1><u>Tuple Methods</u></h1>
<p>tup = (2,1,3,1)</p>
<p>tup.index(el)    #returns index of first occurrence  tup.index(1) is 1</p>
<p>tup.count(el)    #counts total occurrences  tup.count(1) is 2</p>

<h1><u>Dictionary in Python</u></h1>
<h3>Dictionary are used to store data values in key:values pairs</h3>
<h3>They are unordered,mutable(changeable) & don't allow duplicate keys</h3>
<p>dict["name"], dict["cgpa"],dict["marks"]</p>
<p>dic["key"] = "value" #to assign or add new</p>
<hr>

<h1><u>Dictionary in Python</u></h1>
<h3>Nested Dictionaries</h3>
<p>std = {<br>
        "name":"azam"<br>
        "score":{<br>
                "eng":99,<br>
                "maths":88,<br>
                "phy":77 <br>
        }
</p>
<hr>

<h1><u>Dictionary Methods</u></h1>
<p>my.Dict.keys() #return all keys</p>
<p>my.Dict.values() #return all values</p>
<p>my.Dict.items() #returns all(key,val) pairs as tuples</p>
<p>my.Dict.update(newDict) #inserts the specified items to the dictionary</p>
<hr>

<h1><u>Set in Python</u></h1>
<h3>Set is the collection of the unordered items.</h3>
<h3>Each element in the set must be unique & immutable.</h3>
<p>nums = {1,2,3,4}</p>
<p>set2 = {1,2,2,2}</p> #it dont repeate same vlue.
<p>null_set = set()</p>
<hr>

<h1><u>Set Methods</u></h1>
<p>set.add(el)  #adds an element</p>
<p>set.remove(el) #removes the elements</p>
<p>set.clear() #removes the set</p>
<p>set.pop() #removes the random vlue</p>
<p>set.union(set2) #combines both set values & returns new</p>
<p>set.intersection(set2) #combines common values & returns new</p>
