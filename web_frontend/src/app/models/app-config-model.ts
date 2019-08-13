export interface AppConfigModel {
  apiRoot: string;
  steamopenid: {
    return_path: string;
    realm: string;
  };
}
