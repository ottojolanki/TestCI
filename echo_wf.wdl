workflow echo_wf { 

    String say_this

    call echo { input:
        say_what = say_this
    }
}

task echo {

    String say_what

    command {
        ls -l
        pwd
        python /echo.py ${say_what}
    }
    output {
        String what_said = read_lines(stdout())[0]
    }
    runtime {
        docker: "quay.io/ottojolanki/echo:latest"
    }
}