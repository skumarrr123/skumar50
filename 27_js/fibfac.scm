;Team SD :: Suhana Kumar, Danny Huang
;SoftDev PD 5
;W27 -  Basic functions in JavaScript
;2025-01-06
;time: 1

(define fact (lambda (n)
              (if(= n 1)
                 1
                 (* n (fact (- n 1))))))

(define fib (lambda (n)
              (cond
                [(= n 0) 0]
                [(= n 1) 1]
                [else (+ (fib(- n 1)) (fib(- n 2)))])))
(fact 1)
(fib 5)
