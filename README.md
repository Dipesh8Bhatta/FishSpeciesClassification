# Fish Species Classification
This is a Computer vision project. The main aim of this project is to identify the species of fish from the image provided to it.<br>
This work is inspired by the Pokedex project of <b>Adrian Rosebrock(2016)</b>.

In this Readme file I will walk you through to head start the project running.

<ol>
<li>Git clone this project in your machine.</li>

<li>Add two directories: 'dataset' and 'examples' in the cloned project.</li>

<li>Download the fish dataset provided in this link and put it into dataset.</li>

<li>Keep the some images of fish in the examples folder, later on we are using it for prediction.</li>

<li>Now you are good to <b>train your model</b>. We required to pass following arguments to run our command.
    <ul>
        <li>
            <b>--dataset</b> :  to give the path of our dataset.
        </li>
        <li>
            <b>--model</b> :  to give the name under which we are going to save out model.
        </li>
        <li>
            <b>--labelbin</b> :  to give the name under which we are going to save out binarized labels.
        </li>
        <li>
            <b>--plot</b> :  to give the name under which are going to save our plot of performance of this model. This argument is optional since there is a "plot.png" file already set as default
        </li>
    </ul>
    If you are following the above steps our command should look like this:<br>
    <b>"python train.py --dataset dataset --model fishSpeciesClassification.model --labelbin lb.pickle --plot "plot.png"</b> 
</li>

<li>After successfully running above command, you will see three files will generated in the project: "fishSpeciesClassification.model", "lb.pickle" and "plot.png".</li>

<li>Now we can <b>classify fish species images</b>. We need to pass following arguments to run our command.
    <ul>
        <li>
            <b>--model</b> :  to give the path of your saved model.
        </li>
        <li>
            <b>--labelbin</b> :  to give the path of your saved binarized labels.
        </li>
         <li>
            <b>--image</b> :  to give the path the image you are going to classify. Here we are using that images saved in examples directory.
        </li>
    </ul>
    If you are following the above steps our command should look like this:<br>
    <b> "python classify.py --model fishSpeciesClassification.model --labelbin lb.pickle --image examples/fish_species.png"</b>
</li>
</ol>
Now you will see a window popped up to show the classified image as correct and incorrect and it's accuracy percentage.<br>

<p>References:
    <ul>
        <li>Adrian Rosebrock, 2016, <i>Keras and Convolutional Neural Networks (CNNs)</i>, Pyimagesearch, retrieved 7 April 2020 &lt;https://www.pyimagesearch.com&gt; </li>
    </ul>
</p>
