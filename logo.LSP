(defun ins (xy rotation)
(command "_insert" "crest.dxf" xy "0.012" "0.012" rotation)  
)

  
(defun runfile ()
  if (setq f (open "logopoints.txt" "r"))
  (setq counter 1)
  (while
    (setq txtLine(read-line f))
    (setq xyr (substr txtLine 4))
    (setq rotat (substr txtline 1 3))
    (ins xyr rotat)
  )
  )