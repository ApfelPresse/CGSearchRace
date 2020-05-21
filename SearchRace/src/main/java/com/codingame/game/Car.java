package com.codingame.game;

public class Car extends Unit {
    public double angle;
    public String message;
    public boolean debug;
    public int thrust = 0;

    public Point target;

    Car(double x, double y, double angle) {
        super(x, y);
        this.angle = angle;
        this.friction = Constants.CAR_FRICTION;
    }


    public void handleInput(String input, IPlayerManager manager) throws Exception{
        target = null;
        message = "";
        Car car = this;
        String[] splitted = input.split(" ");

        if(splitted[0].equals("EXPERT")){
            int angle = Integer.parseInt(splitted[1]);
            thrust = Integer.parseInt(splitted[2]);
            if(thrust < 0 || thrust > Constants.CAR_MAX_THRUST) {
                manager.addGameSummary("Invalid thrust. Please keep between 0 and " + Constants.CAR_MAX_THRUST);
                throw new Exception( "Invalid thrust");
            }

            if(angle < -18 || angle > 18){
                manager.addGameSummary("Invalid angle. Please keep between -18 and 18.");
                throw new Exception("Invalid angle");
            }

            car.handleExpertInput(angle, thrust);
            if(splitted.length > 3){
                int totalLength = ("EXPERT " +angle+" "+thrust+" ").length();
                car.message = input.substring(totalLength);

                if(car.message.length() > 20){
                    car.message = car.message.substring(0, 20);
                }
            }else{
                car.message="";
            }

        }
        else{
            int x = Integer.parseInt(splitted[0]);
            int y = Integer.parseInt(splitted[1]);
            target = new Point(x, y);
            thrust = Integer.parseInt(splitted[2]);
            if(thrust < 0 || thrust > Constants.CAR_MAX_THRUST) {
                manager.addGameSummary("Invalid thrust. Please keep between 0 and " + Constants.CAR_MAX_THRUST);
                throw new Exception( "Invalid thrust");
            }

            car.handleInput(x, y, thrust);
            if(splitted.length > 3){
                int totalLength = (x+" "+y+" "+thrust+" ").length();
                car.message = input.substring(totalLength);
                if(car.message.length() > 20){
                    car.message = car.message.substring(0, 20);
                }
            }else{
                car.message="";
            }
        }

        if(car.message.contains("debug")){
            debug = true;
        }
    }

    public void handleExpertInput(int angle, int thrust){
        double newAngle = Math.toDegrees(this.angle) + angle;
        this.angle = Math.toRadians(newAngle);
        thrustTowardsHeading(thrust);
    }

    public void handleInput(int x, int y, int thrust){
        if (this.x != x || this.y != y) {
            double angle = this.getAngle(new Point(x, y));
            double relativeAngle = shortAngleDist(this.angle, angle);
            if (Math.abs(relativeAngle) >= Constants.MAX_ROTATION_PER_TURN) {
                angle = this.angle + Constants.MAX_ROTATION_PER_TURN * Math.signum(relativeAngle);
            }

            this.angle = angle;
            thrustTowardsHeading(thrust);
        }
    }


    private void thrustTowardsHeading(int thrust){
        double vx = Math.cos(angle) * thrust;
        double vy = Math.sin(angle) * thrust;

        this.vx += vx;
        this.vy += vy;
    }

    @Override
    public void adjust() {
        super.adjust();
        double degrees = Math.round(Math.toDegrees(angle));
        this.angle = Math.toRadians(degrees);
        while(this.angle > Math.PI*2) this.angle-= Math.PI*2;
        while(this.angle < 0)this.angle+= Math.PI*2;
    }

    private static double shortAngleDist(double a0, double a1) {
        double max = Math.PI * 2;
        double da = (a1 - a0) % max;
        return 2 * da % max - da;
    }
}
