// Re-set the document title
document.title = 'Dynamic Fibonacci Sequence in JavaScript';

// Create a red div in the body of the document
var div = document.createElement('div');
div.setAttribute('class', 'red fib-container');
document.querySelector('body').appendChild(div);

// Label to tell us how to use the program, and then what is being displayed.
var treepara = document.createElement('p');
treepara.textContent = "Move the slider to build a tree.";
div.appendChild(treepara);

// div to hold the slider
var treediv = document.createElement('div');
div.setAttribute('class', 'red fib-container');
div.appendChild(treediv);

// slider object
var treeSlider = document.createElement('input');
treeSlider.setAttribute('type', 'range');
treeSlider.setAttribute('class', 'slider');
treeSlider.setAttribute('min', '0');
treeSlider.setAttribute('max', '11');
treeSlider.setAttribute('value', '5');
treediv.appendChild(treeSlider);

// Add a label so it is clear what Fib value is being displayed.
treeSlider.onchange = function() {
  treepara.textContent = "Fib(" + this.value + ")";
  treeSlide(this);
}

// this takes care of the generating of the divs with thier values
function recursiveBinTree(depth) {
    var newDiv = document.createElement('div');
    var newP = document.createElement('p');
    newDiv.appendChild(newP);
    newDiv.setAttribute('class', 'fib-item');

    if(depth === 0) {
      newP.textContent = 'Fib(0) = 0';
      return newDiv;
    }
    else if(depth === 1) {
      newP.textContent = 'Fib(1) = 1';
      return newDiv;
    }
    else {
      var left = recursiveBinTree(depth-1);
      var cls = left.getAttribute('class');
      left.setAttribute('class', 'fib-left ${cls}');
      newDiv.appendChild(left);

      var right = recursiveBinTree(depth-2);
      cls = right.getAttribute('class');
      right.setAttribute('class', 'fib-right ${cls}');
      newDiv.appendChild(right);

      newP.textContent ='Fib(' + depth + ') = ' + computeFib(depth);
      return newDiv;
    }
}

// this actually computes the fib value
function computeFib(value) {
  if (value === 0) {
    return 0;
  }
  else if(value === 1) {
    return 1;
  }
  else if(value === 2) {
    return 1;
  }
  else {
    return computeFib(value-1) + computeFib(value-2);
  }
}

// this is a helper function to call the computeFib function, it adds the whole tree at the end of the program. 
function treeSlide(me) {
  var form = me.parentNode;
  var value = parseInt(me.value);

  // removes any tree that is already displayed
  var tree = document.querySelector('#tree-of-divs');
  if(tree) {
    tree.remove();
  }
  
  // Creates the tree container, and adds it to the document.
  tree = document.createElement('div');
  tree.id = 'tree-of-divs';
  tree.setAttribute('class', 'fib-container');
  var treeObj = recursiveBinTree(value);
  tree.appendChild(treeObj);

  form.parentNode.appendChild(tree);
}

