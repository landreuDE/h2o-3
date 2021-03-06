#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from .estimator_base import H2OEstimator
import h2o


class H2OGeneralizedLinearEstimator(H2OEstimator):
    """
    Generalized Linear Modeling

    Fits a generalized linear model, specified by a response variable, a set of predictors, and a
    description of the error distribution.

    Parameters
    ----------
      model_id : str
        Destination id for this model; auto-generated if not specified.

      training_frame : str
        Id of the training data frame (Not required, to allow initial validation of model parameters).

      validation_frame : str
        Id of the validation data frame.

      nfolds : int
        Number of folds for N-fold cross-validation (0 to disable or >= 2).
        Default: 0

      seed : int
        Seed for pseudo random number generator (if applicable)
        Default: -1

      keep_cross_validation_predictions : bool
        Whether to keep the predictions of the cross-validation models.
        Default: False

      keep_cross_validation_fold_assignment : bool
        Whether to keep the cross-validation fold assignment.
        Default: False

      fold_assignment : "AUTO" | "Random" | "Modulo" | "Stratified"
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.
        Default: "AUTO"

      fold_column : VecSpecifier
        Column with cross-validation fold index assignment per observation.

      response_column : VecSpecifier
        Response variable column.

      ignored_columns : list(str)
        Names of columns to ignore for training.

      ignore_const_cols : bool
        Ignore constant columns.
        Default: True

      score_each_iteration : bool
        Whether to score during each iteration of model training.
        Default: False

      offset_column : VecSpecifier
        Offset column. This will be added to the combination of columns before applying the link function.

      weights_column : VecSpecifier
        Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it from the
        dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice. Negative
        weights are not allowed.

      family : "gaussian" | "binomial" | "multinomial" | "poisson" | "gamma" | "tweedie"
        Family. Use binomial for classification with logistic regression, others are for regression problems.
        Default: "gaussian"

      tweedie_variance_power : float
        Tweedie variance power
        Default: 0.0

      tweedie_link_power : float
        Tweedie link power
        Default: 1.0

      solver : "AUTO" | "IRLSM" | "L_BFGS" | "COORDINATE_DESCENT_NAIVE" | "COORDINATE_DESCENT"
        AUTO will set the solver based on given data and the other parameters. IRLSM is fast on on problems with small
        number of predictors and for lambda-search with L1 penalty, L_BFGS scales better for datasets with many columns.
        Coordinate descent is experimental (beta).
        Default: "AUTO"

      alpha : list(float)
        distribution of regularization between L1 and L2.

      lambda_ : list(float)
        regularization strength

      lambda_search : bool
        use lambda search starting at lambda max, given lambda is then interpreted as lambda min
        Default: False

      early_stopping : bool
        stop early when there is no more relative improvement on train or validation (if provided)
        Default: True

      nlambdas : int
        number of lambdas to be used in a search
        Default: -1

      standardize : bool
        Standardize numeric columns to have zero mean and unit variance
        Default: True

      missing_values_handling : "Skip" | "MeanImputation"
        Handling of missing values. Either Skip or MeanImputation.
        Default: "MeanImputation"

      compute_p_values : bool
        request p-values computation, p-values work only with IRLSM solver and no regularization
        Default: False

      remove_collinear_columns : bool
        in case of linearly dependent columns remove some of the dependent columns
        Default: False

      intercept : bool
        include constant term in the model
        Default: True

      non_negative : bool
        Restrict coefficients (not intercept) to be non-negative
        Default: False

      max_iterations : int
        Maximum number of iterations
        Default: -1

      objective_epsilon : float
        converge if  objective value changes less than this
        Default: -1.0

      beta_epsilon : float
        converge if  beta changes less (using L-infinity norm) than beta esilon, ONLY applies to IRLSM solver
        Default: 0.0001

      gradient_epsilon : float
        converge if  objective changes less (using L-infinity norm) than this, ONLY applies to L-BFGS solver
        Default: -1.0

      link : "family_default" | "identity" | "logit" | "log" | "inverse" | "tweedie"

        Default: "family_default"

      prior : float
        prior probability for y==1. To be used only for logistic regression iff the data has been sampled and the mean
        of response does not reflect reality.
        Default: -1.0

      lambda_min_ratio : float
        min lambda used in lambda search, specified as a ratio of lambda_max
        Default: -1.0

      beta_constraints : str
        beta constraints

      max_active_predictors : int
        Maximum number of active predictors during computation. Use as a stopping criterium to prevent expensive model
        building with many predictors.
        Default: -1

      interactions : list(str)
        A list of predictor column indices to interact. All pairwise combinations will be computed for the list.

      balance_classes : bool
        Balance training data class counts via over/under-sampling (for imbalanced data).
        Default: False

      class_sampling_factors : list(float)
        Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling factors will
        be automatically computed to obtain class balance during training. Requires balance_classes.

      max_after_balance_size : float
        Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes.
        Default: 5.0

      max_confusion_matrix_size : int
        Maximum size (# classes) for confusion matrices to be printed in the Logs
        Default: 20

      max_hit_ratio_k : int
        Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable)
        Default: 0

      max_runtime_secs : float
        Maximum allowed runtime in seconds for model training. Use 0 to disable.
        Default: 0.0

    Returns
    -------
    A subclass of ModelBase is returned. The specific subclass depends on the machine learning task at hand
    (if it's binomial classification, then an H2OBinomialModel is returned, if it's regression then a
    H2ORegressionModel is returned). The default print-out of the models is shown, but further GLM-specific
    information can be queried out of the object. Upon completion of the GLM, the resulting object has
    coefficients, normalized coefficients, residual/null deviance, aic, and a host of model metrics including
    MSE, AUC (for logistic regression), degrees of freedom, and confusion matrices.
    """
    def __init__(self, **kwargs):
        super(H2OGeneralizedLinearEstimator, self).__init__()
        self._parms = {}
        for name in ["model_id", "training_frame", "validation_frame", "nfolds", "seed",
                     "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment", "fold_assignment",
                     "fold_column", "response_column", "ignored_columns", "ignore_const_cols", "score_each_iteration",
                     "offset_column", "weights_column", "family", "tweedie_variance_power", "tweedie_link_power",
                     "solver", "alpha", "lambda_", "lambda_search", "early_stopping", "nlambdas", "standardize",
                     "missing_values_handling", "compute_p_values", "remove_collinear_columns", "intercept",
                     "non_negative", "max_iterations", "objective_epsilon", "beta_epsilon", "gradient_epsilon", "link",
                     "prior", "lambda_min_ratio", "beta_constraints", "max_active_predictors", "interactions",
                     "balance_classes", "class_sampling_factors", "max_after_balance_size", "max_confusion_matrix_size",
                     "max_hit_ratio_k", "max_runtime_secs"]:
            pname = name[:-1] if name[-1] == '_' else name
            self._parms[pname] = kwargs[name] if name in kwargs else None
        if "Lambda" in kwargs:
            self._parms["lambda"] = kwargs["Lambda"]

    @property
    def training_frame(self):
        return self._parms["training_frame"]

    @training_frame.setter
    def training_frame(self, value):
        self._parms["training_frame"] = value

    @property
    def validation_frame(self):
        return self._parms["validation_frame"]

    @validation_frame.setter
    def validation_frame(self, value):
        self._parms["validation_frame"] = value

    @property
    def nfolds(self):
        return self._parms["nfolds"]

    @nfolds.setter
    def nfolds(self, value):
        self._parms["nfolds"] = value

    @property
    def seed(self):
        return self._parms["seed"]

    @seed.setter
    def seed(self, value):
        self._parms["seed"] = value

    @property
    def keep_cross_validation_predictions(self):
        return self._parms["keep_cross_validation_predictions"]

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, value):
        self._parms["keep_cross_validation_predictions"] = value

    @property
    def keep_cross_validation_fold_assignment(self):
        return self._parms["keep_cross_validation_fold_assignment"]

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, value):
        self._parms["keep_cross_validation_fold_assignment"] = value

    @property
    def fold_assignment(self):
        return self._parms["fold_assignment"]

    @fold_assignment.setter
    def fold_assignment(self, value):
        self._parms["fold_assignment"] = value

    @property
    def fold_column(self):
        return self._parms["fold_column"]

    @fold_column.setter
    def fold_column(self, value):
        self._parms["fold_column"] = value

    @property
    def response_column(self):
        return self._parms["response_column"]

    @response_column.setter
    def response_column(self, value):
        self._parms["response_column"] = value

    @property
    def ignored_columns(self):
        return self._parms["ignored_columns"]

    @ignored_columns.setter
    def ignored_columns(self, value):
        self._parms["ignored_columns"] = value

    @property
    def ignore_const_cols(self):
        return self._parms["ignore_const_cols"]

    @ignore_const_cols.setter
    def ignore_const_cols(self, value):
        self._parms["ignore_const_cols"] = value

    @property
    def score_each_iteration(self):
        return self._parms["score_each_iteration"]

    @score_each_iteration.setter
    def score_each_iteration(self, value):
        self._parms["score_each_iteration"] = value

    @property
    def offset_column(self):
        return self._parms["offset_column"]

    @offset_column.setter
    def offset_column(self, value):
        self._parms["offset_column"] = value

    @property
    def weights_column(self):
        return self._parms["weights_column"]

    @weights_column.setter
    def weights_column(self, value):
        self._parms["weights_column"] = value

    @property
    def family(self):
        return self._parms["family"]

    @family.setter
    def family(self, value):
        self._parms["family"] = value

    @property
    def tweedie_variance_power(self):
        return self._parms["tweedie_variance_power"]

    @tweedie_variance_power.setter
    def tweedie_variance_power(self, value):
        self._parms["tweedie_variance_power"] = value

    @property
    def tweedie_link_power(self):
        return self._parms["tweedie_link_power"]

    @tweedie_link_power.setter
    def tweedie_link_power(self, value):
        self._parms["tweedie_link_power"] = value

    @property
    def solver(self):
        return self._parms["solver"]

    @solver.setter
    def solver(self, value):
        self._parms["solver"] = value

    @property
    def alpha(self):
        return self._parms["alpha"]

    @alpha.setter
    def alpha(self, value):
        self._parms["alpha"] = value

    @property
    def lambda_(self):
        return self._parms["lambda"]

    @lambda_.setter
    def lambda_(self, value):
        self._parms["lambda"] = value

    @property
    def lambda_search(self):
        return self._parms["lambda_search"]

    @lambda_search.setter
    def lambda_search(self, value):
        self._parms["lambda_search"] = value

    @property
    def early_stopping(self):
        return self._parms["early_stopping"]

    @early_stopping.setter
    def early_stopping(self, value):
        self._parms["early_stopping"] = value

    @property
    def nlambdas(self):
        return self._parms["nlambdas"]

    @nlambdas.setter
    def nlambdas(self, value):
        self._parms["nlambdas"] = value

    @property
    def standardize(self):
        return self._parms["standardize"]

    @standardize.setter
    def standardize(self, value):
        self._parms["standardize"] = value

    @property
    def missing_values_handling(self):
        return self._parms["missing_values_handling"]

    @missing_values_handling.setter
    def missing_values_handling(self, value):
        self._parms["missing_values_handling"] = value

    @property
    def compute_p_values(self):
        return self._parms["compute_p_values"]

    @compute_p_values.setter
    def compute_p_values(self, value):
        self._parms["compute_p_values"] = value

    @property
    def remove_collinear_columns(self):
        return self._parms["remove_collinear_columns"]

    @remove_collinear_columns.setter
    def remove_collinear_columns(self, value):
        self._parms["remove_collinear_columns"] = value

    @property
    def intercept(self):
        return self._parms["intercept"]

    @intercept.setter
    def intercept(self, value):
        self._parms["intercept"] = value

    @property
    def non_negative(self):
        return self._parms["non_negative"]

    @non_negative.setter
    def non_negative(self, value):
        self._parms["non_negative"] = value

    @property
    def max_iterations(self):
        return self._parms["max_iterations"]

    @max_iterations.setter
    def max_iterations(self, value):
        self._parms["max_iterations"] = value

    @property
    def objective_epsilon(self):
        return self._parms["objective_epsilon"]

    @objective_epsilon.setter
    def objective_epsilon(self, value):
        self._parms["objective_epsilon"] = value

    @property
    def beta_epsilon(self):
        return self._parms["beta_epsilon"]

    @beta_epsilon.setter
    def beta_epsilon(self, value):
        self._parms["beta_epsilon"] = value

    @property
    def gradient_epsilon(self):
        return self._parms["gradient_epsilon"]

    @gradient_epsilon.setter
    def gradient_epsilon(self, value):
        self._parms["gradient_epsilon"] = value

    @property
    def link(self):
        return self._parms["link"]

    @link.setter
    def link(self, value):
        self._parms["link"] = value

    @property
    def prior(self):
        return self._parms["prior"]

    @prior.setter
    def prior(self, value):
        self._parms["prior"] = value

    @property
    def lambda_min_ratio(self):
        return self._parms["lambda_min_ratio"]

    @lambda_min_ratio.setter
    def lambda_min_ratio(self, value):
        self._parms["lambda_min_ratio"] = value

    @property
    def beta_constraints(self):
        return self._parms["beta_constraints"]

    @beta_constraints.setter
    def beta_constraints(self, value):
        self._parms["beta_constraints"] = value

    @property
    def max_active_predictors(self):
        return self._parms["max_active_predictors"]

    @max_active_predictors.setter
    def max_active_predictors(self, value):
        self._parms["max_active_predictors"] = value

    @property
    def interactions(self):
        return self._parms["interactions"]

    @interactions.setter
    def interactions(self, value):
        self._parms["interactions"] = value

    @property
    def balance_classes(self):
        return self._parms["balance_classes"]

    @balance_classes.setter
    def balance_classes(self, value):
        self._parms["balance_classes"] = value

    @property
    def class_sampling_factors(self):
        return self._parms["class_sampling_factors"]

    @class_sampling_factors.setter
    def class_sampling_factors(self, value):
        self._parms["class_sampling_factors"] = value

    @property
    def max_after_balance_size(self):
        return self._parms["max_after_balance_size"]

    @max_after_balance_size.setter
    def max_after_balance_size(self, value):
        self._parms["max_after_balance_size"] = value

    @property
    def max_confusion_matrix_size(self):
        return self._parms["max_confusion_matrix_size"]

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, value):
        self._parms["max_confusion_matrix_size"] = value

    @property
    def max_hit_ratio_k(self):
        return self._parms["max_hit_ratio_k"]

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, value):
        self._parms["max_hit_ratio_k"] = value

    @property
    def max_runtime_secs(self):
        return self._parms["max_runtime_secs"]

    @max_runtime_secs.setter
    def max_runtime_secs(self, value):
        self._parms["max_runtime_secs"] = value

    @property
    def Lambda(self):
        """[DEPRECATED] Use self.lambda_ instead"""
        return self._parms["lambda"] if "lambda" in self._parms else None
    
    @Lambda.setter
    def lambda_(self, value):
        """[DEPRECATED] Use self.lambda_ instead"""
        self._parms["lambda"] = value
    
    @staticmethod
    def getGLMRegularizationPath(model):
        """
        Extract full regularization path explored during lambda search from glm model.
        @param model - source lambda search model
        """
        x = h2o.api("GET /3/GetGLMRegPath", data={"model": model._model_json["model_id"]["name"]})
        ns = x.pop("coefficient_names")
        res = {
            "lambdas": x["lambdas"],
            "explained_deviance_train": x["explained_deviance_train"],
            "explained_deviance_valid": x["explained_deviance_valid"],
            "coefficients": [dict(zip(ns,y)) for y in x["coefficients"]],
        }
        if "coefficients_std" in x:
            res["coefficients_std"] = [dict(zip(ns,y)) for y in x["coefficients_std"]]
        return res
    
    @staticmethod
    def makeGLMModel(model, coefs, threshold=.5):
        """
        Create a custom GLM model using the given coefficients.
        Needs to be passed source model trained on the dataset to extract the dataset information from.
          @param model - source model, used for extracting dataset information
          @param coefs - dictionary containing model coefficients
          @param threshold - (optional, only for binomial) decision threshold used for classification
        """
        model_json = h2o.api("POST /3/MakeGLMModel", data={"model": model._model_json["model_id"]["name"],
            "names": list(coefs.keys()), "beta": list(coefs.values()), "threshold": threshold})
        m = H2OGeneralizedLinearEstimator()
        m._resolve_model(model_json["model_id"]["name"], model_json)
        return m

