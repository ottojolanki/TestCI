workflow echo_wf { 

    String say_this

    call echo { input:
        say_what = say_this
    }
}

task echo {

    String say_what

    command {
        python /echoz.py ${say_what}
    }
    output {
        String what_said = read_lines(stdout())[0]
    }
    runtime {
        docker: "quay.io/ottojolanki/echo:latest"
    }
}