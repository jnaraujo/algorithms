/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root){
    if(!root)
        return 0;
    
    return 1 + countNodes(root->left) + countNodes(root->right);
}