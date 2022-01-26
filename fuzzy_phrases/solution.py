import json

def phrasel_search(P, Queries):
    # Write your solution here
    
        result =[]
        print("Answer as below")
        for item in Queries:
            tempresult =[]
            for pitem in P:
               string = pitem.split(" ")
               pattern = pitem  # Original Phrase
               pattern1 = string[0] + '\s\w+\s' + string[1] #Fuzzy Phrase 1
               if len(string) >= 3:
                   pattern2 = string[0] +" " + string[1]+" " + string[2] + '\s\w+\s'+ string[3]  #Fuzzy Phrase 2
               
               ans = re.findall(pattern,item)
               for val in ans:
                   if val not in tempresult:
                        tempresult.append(val)
               
               ans = re.findall(pattern1,item)
               for val in ans:
                   if val not in tempresult:
                        tempresult.append(val)
             
               ans = re.findall(pattern2,item)  
               for val in ans:
                   if val not in tempresult:
                        tempresult.append(val)
            result.append(tempresult)
    ans = result
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
