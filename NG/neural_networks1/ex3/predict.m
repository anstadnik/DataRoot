function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

% size(Theta1)	1 layer   m + 1
% size(Theta2) 	num_labels    1 layer + 1
% size(X)		n   m
% size([X; 0])
% size([X 0])
% [ones(m, 1) X]	n	1 layer
% size(Theta2) 	num_labels    1 layer + 1

[~, p] = max([ones(m, 1) sigmoid([ones(m, 1) X] * Theta1')] * Theta2', [], 2);
% size(max([ones(m, 1) [ones(m, 1) X] * Theta1'] * Theta2', [], 2))
% p = max([ones(size(Theta1, 1), 1) ([ones(m, 1) X] * Theta1')] * Theta2');
% p = [ones(size(X, 1), 1) [ones(m, 1) X] * Theta1'];
% size([ones(m, 1) X])
% size(X)






% =========================================================================


end
