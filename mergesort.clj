

(comment "Toma 2 listas ordenadas y devuelve una lista ordenada" )
(defn mergear [l1 l2]
    (cond
        (= (count l1) 0) ;;caso base 1
        l2
        (= (count l2) 0) ;;caso base 2
        l1
        :else
        (if 
            (< (first l1) (first l2))
            (cons (first l1) (mergear (rest l1) l2))
            (cons (first l2) (mergear l1 (rest l2)))
        )
    )
)



(defn mergesort [lista]
    (if
        (<= (count lista) 1)
        lista
        (let [
            q (Math/floor (/ (count lista) 2))
            mitad1 (take q lista)
            mitad2 (drop q lista)
        ]
            (merge (mergesort mitad1) (mergesort mitad2))
        )
    
    )

)

(print (mergesort (list 1 8 7 0 4 3 15 2 2 9)))