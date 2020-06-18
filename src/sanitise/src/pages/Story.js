import React, { Component } from 'react';
import Navbar from '../components/navbar';
import Display from '../components/display';


/**
 * TESTING
 */
class Story extends Component {
    render () {
        return (
            <div>
            <Navbar />
            <Display  
                title={"SANITISE.MEDIA @ UTS"} 
                title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
                paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
                img={"/SampleDisplay.png"} 
                animation={"fadeIn"}
                animateOnce={"true"}>
            </Display>
            <Display    
                title={"SANITISE.MEDIA @ UTS"}
                title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
                paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
                img={"/SampleDisplay.png"} >
            </Display>
            <Display    
                title={"SANITISE.MEDIA @ UTS"}
                title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
                paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
                img={"/SampleDisplay.png"} >
            </Display>
            <Display    
                title={"SANITISE.MEDIA @ UTS"}
                title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
                paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
                img={"/SampleDisplay.png"} >
            </Display>
            </div>
        );
    }
}



export default Story;