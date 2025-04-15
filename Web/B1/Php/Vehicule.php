<?php
abstract class Vehicule
{
    protected $brand;
    protected $model;
    protected $year;

    function getBrand()
    {
        return $this->brand;
    }
    function getModel()
    {
        return $this->model;
    }
    function getYear()
    {
        return $this->year;
    }

    function setBrand($brand)
    {
        $this->brand = $brand;
    }
    function setModel($model)
    {
        $this->model = $model;
    }
    function setYear($year)
    {
        $this->year = $year;
    }
}
