(defun ins (xy rotation)

  (command ".insert" "crest.dwg" xy "1" "1" rotation
	   "_.explode" "_last" ""
	   )
  

  
)

  
(defun runfile ()
  if (setq f (open "logopoints.txt" "r"))
  (while
    (setq txtLine(read-line f))
    (setq xyr (substr txtLine 4))
    (setq rotat (substr txtline 1 3))
    (ins xyr rotat)
  )

)
(runfile)