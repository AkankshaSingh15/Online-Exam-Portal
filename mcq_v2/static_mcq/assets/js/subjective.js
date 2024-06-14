function showq1(bool_value){
    document.getElementById('q1').style.display="block";
    document.getElementById('q2').style.display="none";
    document.getElementById('q3').style.display="none";
    document.getElementById('q4').style.display="none";
    document.getElementById('q5').style.display="none";
    document.getElementById('q6').style.display="none";
    if (!bool_value) {  
        document.getElementById('b1').style.border="1.5px solid #FF1744";
      }
    }
    function showq2(bool_value){
        document.getElementById('q1').style.display="none";
        document.getElementById('q2').style.display="block";
        document.getElementById('q3').style.display="none";
        document.getElementById('q4').style.display="none";
        document.getElementById('q5').style.display="none";
        document.getElementById('q6').style.display="none";
        if (!bool_value) {  
            document.getElementById('b2').style.border="1.5px solid #FF1744";
            document.getElementById('b1').style.border="1.5px solid #00bfff";
          }
        }
        function showq3(bool_value){
            document.getElementById('q1').style.display="none";
            document.getElementById('q2').style.display="none";
            document.getElementById('q3').style.display="block";
            document.getElementById('q4').style.display="none";
            document.getElementById('q5').style.display="none";
            document.getElementById('q6').style.display="none";
            if (!bool_value) {  
                document.getElementById('b3').style.border="1.5px solid #FF1744";
                document.getElementById('b2').style.border="1.5px solid #00bfff";
              }
            }
            function showq4(bool_value){
                document.getElementById('q1').style.display="none";
                document.getElementById('q2').style.display="none";
                document.getElementById('q3').style.display="none";
                document.getElementById('q4').style.display="block";
                document.getElementById('q5').style.display="none";
                document.getElementById('q6').style.display="none";
                if (!bool_value) {  
                    document.getElementById('b4').style.border="1.5px solid #FF1744";
                    document.getElementById('b3').style.border="1.5px solid #00bfff";
                  }
                }
                function showq5(bool_value){
                    document.getElementById('q1').style.display="none";
                    document.getElementById('q2').style.display="none";
                    document.getElementById('q3').style.display="none";
                    document.getElementById('q4').style.display="none";
                    document.getElementById('q5').style.display="block";
                    document.getElementById('q6').style.display="none";
                    if (!bool_value) {  
                        document.getElementById('b5').style.border="1.5px solid #FF1744";
                        document.getElementById('b4').style.border="1.5px solid #00bfff";
                      }
                    }
                    function showq6(bool_value){
                        document.getElementById('q1').style.display="none";
                        document.getElementById('q2').style.display="none";
                        document.getElementById('q3').style.display="none";
                        document.getElementById('q4').style.display="none";
                        document.getElementById('q5').style.display="none";
                        document.getElementById('q6').style.display="block";
                        if (!bool_value) {  
                            document.getElementById('b6').style.border="1.5px solid #FF1744";
                            document.getElementById('b5').style.border="1.5px solid #00bfff";
                          }
                        }
                    // function showq7(bool_value){
                    //         document.getElementById('q1').style.display="none";
                    //         document.getElementById('q2').style.display="none";
                    //         document.getElementById('q3').style.display="none";
                    //         document.getElementById('q4').style.display="none";
                    //         document.getElementById('q5').style.display="none";
                    //         document.getElementById('q6').style.display="none";
                    //         document.getElementById('q7').style.display="block";
                    //         if (!bool_value) {  
                    //             document.getElementById('b7').style.border="1.5px solid #FF1744";
                    //             document.getElementById('b6').style.border="1.5px solid #00bfff";
                    //           }
                    //         }