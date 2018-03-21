(comment "PARA EJECUTARLO, CORRER lein exec hacerAzar.clj 20 veint.csv")

(defn -main [cantidad archivo] 
  (spit archivo 
    (clojure.string/join "," 
      (map  (fn [x] (str (rand))) (range (Integer/parseInt cantidad)))
    )
  ) 
)
(comment "ESTO ES PARA QUE LEIN EXEC PUEDA PASAR ARGUMENTOS")
(try (require 'leiningen.exec)
     (when @(ns-resolve 'leiningen.exec '*running?*)
       (apply -main (rest *command-line-args*)))
     (catch java.io.FileNotFoundException e))

