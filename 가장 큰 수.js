function solution(numbers) {
    
    var answer = numbers.map(c=> c + '').
    				sort((a,b) => (b+a) - (a+b)).join('');
    
    return answer[0]==='0'? '0' : answer;
    // 문자로 치완하여 두문자를 합하여 비교한 유니코드값이 큰쪽으로 
}