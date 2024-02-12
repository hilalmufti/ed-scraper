(ns ed-scraper.core
  (:require [clj-http.client :as client]
            [clojure.repl :refer :all]
            [clojure.edn :as edn]))

(defn get-token 
  ([] (:ed-api-token (edn/read-string (slurp "config.edn"))))
  ([file] (:ed-api-token (edn/read-string (slurp file)))))

(def token (get-token))

(client/get "https://us.edstem.org/api/user" {:headers {"Authorization" (str "Bearer " token)}})