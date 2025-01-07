
//Team SD :: Suhana Kumar, Danny Huang
//SoftDev PD 5
//W27 - Intro to JS
//2025-01-06
//time: 1

//factorial:

//<your team's fact(n) implementation>
let fact = function(n){
    if (n == 1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}
//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1)
fact(2)
fact(3)
fact(4)
fact(5)

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
let fib = function(n){
    if(n == 0){
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
}
//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(1)
fib(2)
fib(3)
fib(4)
fib(5)
//=================================================================
