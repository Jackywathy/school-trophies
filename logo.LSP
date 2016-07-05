(defun _insert (xy rotation)
  (command ".insert" "schoolcrest.dwg" xy "1" "1" rotation)
)

  
(defun C:runfile ()
  (setq readVal (getint "Enter Number of Trophies, Default (10)"))
  (setq counter 0)
  (if (= readVal nil)
    (setq readVal 10)
    )
  
  (cond ((= (findfile "logopoints.txt") nil) ; if it cant find the file
	(prompt "Fatal Error - Cannot find logopoints.txt")
	 ); end of first condition
	((= (findfile "schoolcrest.dwg") nil) ; if school crest is found
	 (prompt "Fatal Error - Cannot find schoolcrest.dwg")
	 ); end of second condition
	(T  ;else do the actual insertions
	 (setq file (open (findfile "logopoints.txt") "r")); open file as file
         (while (and (setq txtLine (read-line file))
		     (< counter readVal)
		     )
	     (setq counter (1+ counter))
             (setq xyr (substr txtLine 4))
             (setq rotat (substr txtline 1 3))
             (_insert xyr rotat)
         )
	 )
	)
  (command "_regenall")
  )